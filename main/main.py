"""
main.py — основной файл Telegram-бота для просмотра расписания групп ТИУ

Запуск:
    python main.py

Бот позволяет:
- выбрать отделение, специальность и группу
- сохранить основную группу пользователя
- просматривать расписание по ссылке
- работать с алиасами (альтернативными названиями групп)

Требования:
- Python 3.8+
- python-telegram-bot
- файл groups_full.py с актуальными группами
- файл secrets.py с токеном Telegram-бота

"""

from typing import Optional, Dict, Tuple
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, MenuButton, MenuButtonCommands, Message
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from telegram.error import NetworkError, BadRequest
import re
import datetime
import time
import threading
from urllib.parse import urlparse
import os
from playwright.async_api import async_playwright
import tempfile
from functools import lru_cache
import json
import logging
from aiohttp import web

from .secrets import secret_key
from .groups_full import GROUPS_FULL, get_group_by_name
from .user_data import set_user_group, get_user_group
from .bells import format_bells_message, format_time_left_message

# --- Константы ---
MIN_MESSAGE_INTERVAL = 1  # Уменьшаем интервал между сообщениями до 1 секунды
SCREENSHOT_TIMEOUT = 5000
PAGE_LOAD_TIMEOUT = 30000
CACHE_TIMEOUT = 300
MAX_RETRIES = 2
RETRY_DELAY = 2
WEBHOOK_HOST = "your-domain.com"  # Замените на ваш домен
WEBHOOK_PORT = 8443  # Порт для вебхука
WEBHOOK_URL = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}/webhook"  # URL для вебхука
WEBHOOK_CERT = "path/to/cert.pem"  # Путь к SSL сертификату

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Сообщения и константы ---
WELCOME_BASE = "👋 Привет! Я бот для просмотра расписания занятий."
CHOOSE_ACTION = "Выберите действие:"
CHOOSE_DEPARTMENT = "Выбери отделение:"
CHOOSE_SPECIALTY = "Выбери специальность:"
CHOOSE_GROUP = "Выберите группу:"
CHOOSE_MAIN_GROUP = "Выберите вашу основную группу:"
SAVED_GROUP = "📚 Ваша сохраненная группа: {group_name}"
SAVED_MAIN_GROUP = "Группа {group_name} сохранена как ваша основная группа!"
FORMING_SCHEDULE = "Формирую расписание для группы {group_name}, подожди немного..."
ERROR_SITE = "Ошибка: Не удалось получить доступ к сайту. Возможно, сайт временно недоступен или URL некорректен."
ERROR_GENERIC = "Ошибка: {error_message}"
RETRY = "Попробовать еще раз?"
ONLY_SCHEDULE_URL = "Можно отправлять только ссылки на сайт расписания!"
INVALID_INPUT = "Пожалуйста, введите корректное название группы или URL."
SCREENSHOT_ERROR = "Не удалось сделать скриншот расписания. Попробуйте позже."

# --- Декоратор для логирования ошибок ---
def log_exceptions(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"Exception in {func.__name__}: {e}")
            if isinstance(e, NetworkError):
                await send_bot_text(args[0], args[1], ERROR_SITE)
            else:
                await send_bot_text(args[0], args[1], ERROR_GENERIC.format(error_message=str(e)))
    return wrapper

# --- Кэширование и состояние ---
last_message_ids: Dict[int, int] = {}
user_chat_ids: Dict[int, int] = {}
last_message_time: Dict[int, float] = {}
schedule_cache: Dict[str, Tuple[str, float]] = {}  # url -> (screenshot_path, timestamp)

# --- Клавиатуры ---
def get_main_keyboard(saved_group: Optional[str] = None) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("Выбрать отделение", callback_data="select_department")],
        [InlineKeyboardButton("Расписание звонков", callback_data="show_bells")]
    ]
    if saved_group and saved_group in GROUPS_FULL:
        keyboard.append([
            InlineKeyboardButton("Расписание моей группы", callback_data="show_my_group"),
            InlineKeyboardButton("Изменить мою группу", callback_data="change_my_group")
        ])
    else:
        keyboard.append([
            InlineKeyboardButton("Добавить мою группу", callback_data="change_my_group")
        ])
    return InlineKeyboardMarkup(keyboard)

def get_welcome_message(saved_group: Optional[str] = None, is_after_save: bool = False) -> str:
    if is_after_save:
        return CHOOSE_ACTION
    
    msg = WELCOME_BASE
    if saved_group and saved_group in GROUPS_FULL:
        msg += f"\n\n{SAVED_GROUP.format(group_name=GROUPS_FULL[saved_group]['name'])}"
    
    # Добавляем информацию о текущем времени
    time_info = format_time_left_message()
    msg += f"\n\n{time_info}"
    
    msg += "\n\nВыберите действие:"
    return msg

@lru_cache(maxsize=100)
def is_valid_url(url: str) -> bool:
    """Проверяет, является ли URL валидным."""
    url_pattern = re.compile(
        r'^https?://'  # http:// или https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(url_pattern.match(url))

@lru_cache(maxsize=100)
def is_allowed_schedule_url(url: str) -> bool:
    """Проверяет, что это ссылка на сайт расписания."""
    try:
        parsed = urlparse(url)
        return parsed.netloc == "coworking.tyuiu.ru"
    except Exception:
        return False

async def update_welcome_message(context: ContextTypes.DEFAULT_TYPE, user_id: int):
    """Обновляет приветственное сообщение с актуальным временем."""
    if user_id in last_message_ids and user_id in user_chat_ids:
        try:
            saved_group = get_user_group(user_id)
            welcome_message = get_welcome_message(saved_group)
            reply_markup = get_main_keyboard(saved_group)
            
            await context.bot.edit_message_text(
                chat_id=user_chat_ids[user_id],
                message_id=last_message_ids[user_id],
                text=welcome_message,
                reply_markup=reply_markup
            )
        except BadRequest as e:
            print(f"Error updating welcome message: {e}")

@lru_cache(maxsize=1000)
def get_cached_schedule(url: str) -> Optional[str]:
    """Получает расписание из кэша, если оно еще актуально."""
    if url in schedule_cache:
        screenshot_path, timestamp = schedule_cache[url]
        if time.time() - timestamp < CACHE_TIMEOUT:
            return screenshot_path
        # Удаляем устаревший кэш
        try:
            os.unlink(screenshot_path)
        except Exception:
            pass
        del schedule_cache[url]
    return None

def cache_schedule(url: str, screenshot_path: str):
    """Сохраняет расписание в кэш."""
    schedule_cache[url] = (screenshot_path, time.time())

async def get_schedule_screenshot(url: str) -> Optional[str]:
    """Делает скриншот страницы расписания и возвращает путь к файлу."""
    # Проверяем кэш
    cached_path = get_cached_schedule(url)
    if cached_path:
        return cached_path

    for attempt in range(MAX_RETRIES):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
            )
            page = await context.new_page()
            try:
                # Загружаем страницу с оптимизированными параметрами
                response = await page.goto(
                    url,
                    wait_until='domcontentloaded',
                    timeout=PAGE_LOAD_TIMEOUT
                )
                
                if not response:
                    if attempt < MAX_RETRIES - 1:
                        await asyncio.sleep(RETRY_DELAY)
                        continue
                    raise Exception("Failed to load page after multiple attempts")
                
                # Ждем загрузки контента с оптимизированными таймаутами
                try:
                    await page.wait_for_load_state('networkidle', timeout=SCREENSHOT_TIMEOUT)
                    
                    # Проверяем наличие элементов загрузки
                    loading_selectors = ['#loading', '.loading', '[class*="loading"]', '[id*="loading"]']
                    for selector in loading_selectors:
                        try:
                            loading = await page.wait_for_selector(selector, timeout=2000)
                            if loading:
                                await loading.wait_for_element_state('hidden', timeout=5000)
                        except Exception:
                            continue
                    
                    # Ждем появления таблицы
                    try:
                        await page.wait_for_selector('table', timeout=SCREENSHOT_TIMEOUT)
                    except Exception as e:
                        # Проверяем наличие сообщения об ошибке
                        error_text = await page.evaluate('''() => {
                            const errorElements = document.querySelectorAll('*');
                            for (const el of errorElements) {
                                if (el.textContent.includes('ошибк') || 
                                    el.textContent.includes('не найдено') || 
                                    el.textContent.includes('нет данных')) {
                                    return el.textContent;
                                }
                            }
                            return null;
                        }''')
                        if error_text:
                            raise Exception(f"Schedule error: {error_text}")
                        raise e
            
                    # Создаем временный файл и делаем скриншот
                    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                        await page.screenshot(path=tmp.name, full_page=True)
                        screenshot_path = tmp.name
                        # Кэшируем результат
                        cache_schedule(url, screenshot_path)
                    return screenshot_path
                    
                except Exception as e:
                    if attempt < MAX_RETRIES - 1:
                        await asyncio.sleep(RETRY_DELAY)
                        continue
                    raise e
                    
            except Exception as e:
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(RETRY_DELAY)
                    continue
                raise e
            finally:
                await browser.close()
    
            return None

async def send_schedule_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE, url: str):
    """Отправляет скриншот расписания пользователю."""
    try:
        screenshot_path = await get_schedule_screenshot(url)
        if screenshot_path:
            try:
                with open(screenshot_path, 'rb') as photo:
                    await update.effective_chat.send_photo(
                        photo=photo,
                        disable_notification=True  # Отключаем уведомления для ускорения
                    )
            finally:
                # Не удаляем файл, если он в кэше
                if url not in schedule_cache:
                    try:
                        os.unlink(screenshot_path)
                    except Exception:
                        pass
        else:
            await send_bot_text(update, context, SCREENSHOT_ERROR)
    except Exception as e:
        print(f"Error sending screenshot: {e}")
        await send_bot_text(update, context, SCREENSHOT_ERROR)

@log_exceptions
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "back_to_menu":
        await start(update, context)
        return
        
    if query.data == "show_bells":
        bells_message = format_bells_message()
        await send_bot_text(update, context, bells_message)
        return
        
    if query.data == "change_my_group":
        context.user_data["is_saving_main"] = True
        departments = ["АиЭС", "МПН", "НГО", "СОНХ", "ПО"]
        keyboard = [[InlineKeyboardButton(dep, callback_data=f"department_{i}")] for i, dep in enumerate(departments)]
        keyboard.append([InlineKeyboardButton("Назад", callback_data="back_to_menu")])
        await send_bot_text(update, context, CHOOSE_DEPARTMENT, reply_markup=InlineKeyboardMarkup(keyboard))
        return
    if query.data == "select_department":
        departments = ["АиЭС", "МПН", "НГО", "СОНХ", "ПО"]
        keyboard = [[InlineKeyboardButton(dep, callback_data=f"department_{i}")] for i, dep in enumerate(departments)]
        keyboard.append([InlineKeyboardButton("Назад", callback_data="back_to_menu")])
        await send_bot_text(update, context, CHOOSE_DEPARTMENT, reply_markup=InlineKeyboardMarkup(keyboard))
        return
    if query.data.startswith("department_"):
        dep_idx = int(query.data.replace("department_", ""))
        departments = ["АиЭС", "МПН", "НГО", "СОНХ", "ПО"]
        dep_name = departments[dep_idx]
        
        # Получаем список специальностей для выбранного отделения
        specialties = set()  # Используем set для уникальных значений
        
        for g in GROUPS_FULL.values():
            if g.get("department") == dep_name:
                specialty = g.get("specialty")
                if specialty:  # Проверяем, что специальность не пустая
                    specialties.add(specialty)
        
        specialties = sorted(list(specialties))  # Преобразуем set в отсортированный список
        
        if specialties:
            keyboard = [[InlineKeyboardButton(spec, callback_data=f"specialty_{spec}")] for spec in specialties]
            keyboard.append([InlineKeyboardButton("Назад", callback_data="select_department")])
            await send_bot_text(update, context, CHOOSE_SPECIALTY, reply_markup=InlineKeyboardMarkup(keyboard))
            return
        else:
            # Если специальностей нет, сразу показываем группы
            await show_groups(update, context, department=dep_name)
            return
    if query.data.startswith("specialty_"):
        specialty = query.data.replace("specialty_", "")
        await show_groups(update, context, department="СОНХ", specialty=specialty)
        return
    if query.data == "show_my_group":
        user_id = update.effective_user.id
        saved_group = get_user_group(user_id)
        if saved_group and saved_group in GROUPS_FULL:
            group_data = GROUPS_FULL[saved_group]
            url = group_data["url"]
            await send_bot_text(update, context, FORMING_SCHEDULE.format(group_name=group_data['name']))
            await send_schedule_screenshot(update, context, url)
            reply_markup = get_group_action_keyboard(url)
            await send_bot_text(update, context, CHOOSE_ACTION, reply_markup=reply_markup)
        return
    if query.data.startswith("group_"):
        group_id = query.data.replace("group_", "")
        group_data = GROUPS_FULL[group_id]
        url = group_data["url"]
        is_saving_main = context.user_data.get("is_saving_main", False)
        if is_saving_main:
            user_id = update.effective_user.id
            set_user_group(user_id, group_id)
            context.user_data["is_saving_main"] = False
            await send_persistent_text(update, context, SAVED_MAIN_GROUP.format(group_name=group_data['name']))
            await start(update, context, is_after_save=True)
            return
        await send_bot_text(update, context, FORMING_SCHEDULE.format(group_name=group_data['name']))
        await send_schedule_screenshot(update, context, url)
        reply_markup = get_group_action_keyboard(url)
        await send_bot_text(update, context, CHOOSE_ACTION, reply_markup=reply_markup)

@log_exceptions
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    main_name, group_info = get_group_by_name(text)
    if group_info:
        group_id = None
        for gid, gdata in GROUPS_FULL.items():
            if gdata["name"] == main_name:
                group_id = gid
                break
        if group_id:
            url = GROUPS_FULL[group_id]["url"]
            user_id = update.effective_user.id
            set_user_group(user_id, group_id)
            # Отправляем сообщения параллельно
            await asyncio.gather(
                send_bot_text(update, context, FORMING_SCHEDULE.format(group_name=main_name)),
                send_schedule_screenshot(update, context, url)
            )
            reply_markup = get_group_action_keyboard(url)
            await send_bot_text(update, context, CHOOSE_ACTION, reply_markup=reply_markup)
            return
    if not text.startswith("http"):
        text = "http://" + text
    if not is_valid_url(text):
        await send_bot_text(update, context, INVALID_INPUT)
        return
    if not is_allowed_schedule_url(text):
        await send_bot_text(update, context, ONLY_SCHEDULE_URL)
        return
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Открыть сайт", url=text)],
        [InlineKeyboardButton("Назад в меню", callback_data="back_to_menu")]
    ])
    await send_bot_text(update, context, CHOOSE_ACTION, reply_markup=reply_markup)

@log_exceptions
async def handle_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик любых сообщений.
    Отправляет приветственное сообщение, когда пользователь открывает чат.
    """
    user_id = update.effective_user.id
    current_time = time.time()
    
    # Проверяем, прошло ли достаточно времени с последнего сообщения
    if user_id not in last_message_ids or (current_time - last_message_time[user_id]) >= MIN_MESSAGE_INTERVAL:
        saved_group = get_user_group(user_id)
        welcome_message = get_welcome_message(saved_group)
        reply_markup = get_main_keyboard(saved_group)
        await send_bot_text(update, context, welcome_message, reply_markup=reply_markup)
        last_message_time[user_id] = current_time
        
        # Если это текстовое сообщение, продолжаем его обработку
        if update.message and update.message.text:
            await handle_message(update, context)

@log_exceptions
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик данных от Web App."""
    try:
        data = json.loads(update.effective_message.web_app_data.data)
        if data.get("action") == "send_screenshot":
            url = data.get("url")
            if url:
                await send_bot_text(update, context, FORMING_SCHEDULE.format(group_name="группы"))
                await send_schedule_screenshot(update, context, url)
                reply_markup = get_group_action_keyboard(url)
                await send_bot_text(update, context, CHOOSE_ACTION, reply_markup=reply_markup)
            else:
                await send_bot_text(update, context, "Ошибка: URL не указан")
    except Exception as e:
        print(f"Error handling webapp data: {e}")
        await send_bot_text(update, context, ERROR_GENERIC.format(error_message=str(e)))

# --- Утилиты для отправки сообщений ---
async def send_bot_text(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str, reply_markup: Optional[InlineKeyboardMarkup] = None) -> Optional[Message]:
    """Отправляет текстовое сообщение, удаляя предыдущее сообщение от бота."""
    user_id = update.effective_user.id
    current_time = time.time()
    
    # Проверяем интервал между сообщениями
    if user_id in last_message_time and current_time - last_message_time[user_id] < MIN_MESSAGE_INTERVAL:
        return None
        
    last_msg_id = context.user_data.get("last_bot_text_id")
    if last_msg_id:
        try:
            await update.effective_chat.delete_message(last_msg_id)
        except Exception:
            pass
            
    try:
        # Используем более быстрый метод отправки
        if hasattr(update, "message") and update.message:
            msg = await update.message.reply_text(
                text,
                reply_markup=reply_markup,
                parse_mode='HTML',  # Используем HTML для более быстрой обработки
                disable_web_page_preview=True  # Отключаем предпросмотр ссылок для ускорения
            )
        else:
            msg = await update.callback_query.message.reply_text(
                text,
                reply_markup=reply_markup,
                parse_mode='HTML',
                disable_web_page_preview=True
            )
            
        context.user_data["last_bot_text_id"] = msg.message_id
        last_message_time[user_id] = current_time
        return msg
    except Exception as e:
        print(f"Error sending message: {e}")
        return None

async def send_persistent_text(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str, reply_markup: Optional[InlineKeyboardMarkup] = None) -> Optional[Message]:
    """Отправляет сообщение без удаления предыдущих."""
    try:
        if hasattr(update, "message") and update.message:
            return await update.message.reply_text(
                text,
                reply_markup=reply_markup,
                parse_mode='HTML',
                disable_web_page_preview=True
            )
        else:
            return await update.callback_query.message.reply_text(
                text,
                reply_markup=reply_markup,
                parse_mode='HTML',
                disable_web_page_preview=True
            )
    except Exception as e:
        print(f"Error sending persistent message: {e}")
        return None

def get_group_id_by_name(main_name: str) -> Optional[str]:
    """Возвращает ID группы по основному названию."""
    for gid, gdata in GROUPS_FULL.items():
        if gdata["name"] == main_name:
            return gid
    return None

# --- Оптимизированные функции ---
@log_exceptions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE, is_after_save: bool = False):
    """
    Обработчик команды /start.
    Отправляет приветственное сообщение с информацией о текущем времени.
    """
    await context.bot.set_my_commands([("start", "Показать меню")])
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    
    # Удаляем предыдущее сообщение, если оно есть
    if user_id in last_message_ids:
        try:
            await context.bot.delete_message(chat_id=user_chat_ids[user_id], message_id=last_message_ids[user_id])
        except BadRequest:
            pass
    
    saved_group = get_user_group(user_id)
    welcome_message = get_welcome_message(saved_group, is_after_save)
    reply_markup = get_main_keyboard(saved_group)
    message = await send_bot_text(update, context, welcome_message, reply_markup=reply_markup)
    
    # Сохраняем ID сообщения и chat_id
    if message:
        last_message_ids[user_id] = message.message_id
        user_chat_ids[user_id] = chat_id

def get_groups_keyboard(filtered, department=None, specialty=None, is_saving_main=False) -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(gdata["name"], callback_data=f"group_{gid}")] for gid, gdata in filtered]
    # Кнопка назад
    if specialty:
        keyboard.append([InlineKeyboardButton("Назад", callback_data="department_3")])
    elif department:
        keyboard.append([InlineKeyboardButton("Назад", callback_data="select_department")])
    else:
        keyboard.append([InlineKeyboardButton("Назад", callback_data="back_to_menu")])
    return InlineKeyboardMarkup(keyboard)

def get_group_action_keyboard(url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Открыть расписание", url=url)],
        [InlineKeyboardButton("Назад в меню", callback_data="back_to_menu")]
    ])

def get_retry_keyboard(callback_data: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("Попробовать снова", callback_data=callback_data)]])

@log_exceptions
async def show_groups(update: Update, context: ContextTypes.DEFAULT_TYPE, department: Optional[str]=None, specialty: Optional[str]=None, is_saving_main: bool=False):
    query = update.callback_query
    await query.answer()
    if is_saving_main:
        context.user_data["is_saving_main"] = True
    filtered = GROUPS_FULL.items()
    if department:
        filtered = [(gid, gdata) for gid, gdata in filtered if gdata.get("department") == department]
    if specialty:
        filtered = [(gid, gdata) for gid, gdata in filtered if gdata.get("specialty") == specialty]
    title = CHOOSE_GROUP
    if is_saving_main:
        title = CHOOSE_MAIN_GROUP
    elif department and specialty:
        title = f"{CHOOSE_GROUP} {department}, {CHOOSE_SPECIALTY} {specialty}:"
    elif department:
        title = f"{CHOOSE_GROUP} {department}:"
    reply_markup = get_groups_keyboard(filtered, department, specialty, is_saving_main)
    await send_bot_text(update, context, title, reply_markup=reply_markup)

async def update_all_welcome_messages(context: ContextTypes.DEFAULT_TYPE):
    """Обновляет приветственные сообщения для всех активных пользователей."""
    current_time = time.time()
    for user_id in list(last_message_ids.keys()):
        try:
            # Проверяем, прошло ли достаточно времени с последнего обновления
            if user_id in last_message_time and current_time - last_message_time[user_id] < MIN_MESSAGE_INTERVAL:
                continue
            await update_welcome_message(context, user_id)
        except Exception as e:
            print(f"Error updating welcome message for user {user_id}: {e}")
            # Если сообщение не найдено, удаляем его из кэша
            if isinstance(e, BadRequest) and "message not found" in str(e).lower():
                if user_id in last_message_ids:
                    del last_message_ids[user_id]
                if user_id in user_chat_ids:
                    del user_chat_ids[user_id]

async def webhook_handler(request: web.Request) -> web.Response:
    """Обработчик вебхуков от Telegram."""
    try:
        update = Update.de_json(await request.json(), request.app['bot'])
        await request.app['dispatcher'].process_update(update)
        return web.Response()
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        return web.Response(status=500)

async def setup_webhook(application):
    """Настройка вебхука."""
    await application.bot.set_webhook(
        url=WEBHOOK_URL,
        certificate=open(WEBHOOK_CERT, 'rb')
    )

async def remove_webhook(application):
    """Удаление вебхука."""
    await application.bot.delete_webhook()

def main():
    """
    Запуск Telegram-бота с использованием вебхуков.
    """
    # Создаем приложение
    app = ApplicationBuilder().token(secret_key).build()
    
    # Добавляем обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    
    # Добавляем задачу обновления времени каждую минуту
    job_queue = app.job_queue
    job_queue.run_repeating(update_all_welcome_messages, interval=60)
    
    # Создаем aiohttp приложение
    web_app = web.Application()
    web_app['bot'] = app.bot
    web_app['dispatcher'] = app
    
    # Добавляем обработчик вебхука
    web_app.router.add_post('/webhook', webhook_handler)
    
    # Настраиваем вебхук при запуске
    app.post_init = setup_webhook
    app.post_shutdown = remove_webhook
    
    # Запускаем веб-сервер
    logger.info("Bot started with webhook...")
    web.run_app(
        web_app,
        host='0.0.0.0',
        port=WEBHOOK_PORT,
        ssl_context={
            'cert': WEBHOOK_CERT,
            'key': WEBHOOK_CERT.replace('.pem', '.key')
        }
    )

if __name__ == '__main__':
    main()