import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import re
import json
from departments_config import departments

# --- НАСТРОЙКИ ---
SELECTION_URL = departments["МПН"]["selection_url"]  # URL страницы с выбором группы
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"  # User-Agent для браузера
OUTPUT_FILE = "groups_full МПН.py"  # Куда сохранять результат

# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---
def make_aliases(name: str) -> list:
    """
    Генерирует список альтернативных написаний (алиасов) для группы.
    Это нужно, чтобы бот мог находить группу по разным вариантам ввода.
    """
    base = name.replace('(', '').replace(')', '').replace('-', ' ').replace('  ', ' ')
    base_noskob = name.replace('(', '').replace(')', '')
    base_dash = name.replace('(', '').replace(')', '').replace(' ', '-')
    base_nodash = name.replace('-', ' ').replace('(', '').replace(')', '')
    aliases = set()
    variants = [
        name,
        name.upper(),
        name.lower(),
        base,
        base.upper(),
        base.lower(),
        base_noskob,
        base_noskob.upper(),
        base_noskob.lower(),
        base_dash,
        base_dash.upper(),
        base_dash.lower(),
        base_nodash,
        base_nodash.upper(),
        base_nodash.lower(),
    ]
    # Добавляем вариант с пробелами вместо дефисов и без скобок
    spaced = name.replace('(', '').replace(')', '').replace('-', ' ')
    spaced = ' '.join(spaced.split())
    variants.extend([spaced, spaced.lower(), spaced.upper()])
    # Добавляем .title() для всех вариантов (например, Спт 23 9 1)
    for v in list(variants):
        variants.append(v.title())
    aliases.update(variants)
    return list(aliases)

def parse_department_and_specialty(group_name: str) -> tuple:
    """
    Пытается определить отделение и специальность по названию группы.
    Для большинства групп ТИУ достаточно первых букв до дефиса.
    """
    # Пример: 'ЗОт-22-(9)-1' -> ('СОНХ', 'ЗОт')
    if group_name.startswith("ЗОт") or group_name.startswith("ЗУт") or group_name.startswith("ИСПт") or group_name.startswith("РПКт") or group_name.startswith("СПт") or group_name.startswith("ЭБКт") or group_name.startswith("ЭГНт"):
        department = "СОНХ"
        specialty = group_name.split('-')[0]
        return department, specialty
    # Если не удалось определить — возвращаем 'Другое'
    return "Другое", group_name.split('-')[0]

async def extract_groups_full() -> dict:
    """
    Парсит сайт расписания и возвращает структуру для groups_full МПН.py.
    Использует Playwright для автоматизации браузера.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=USER_AGENT)
        page = await context.new_page()
        print("Переходим на страницу выбора группы...")
        await page.goto(SELECTION_URL, timeout=60000)
        await asyncio.sleep(7)  # Ждём загрузки страницы
        frame = None
        for attempt in range(10):
            frames = page.frames
            for f in frames:
                if f.url and f.url.startswith(departments["МПН"]["frame_url"]):
                    frame = f
                    print(f"Найден фрейм расписания: {frame.url}")
                    break
            if frame:
                break
            print(f"Фрейм не найден, попытка {attempt+1}/10, жду...")
            await asyncio.sleep(2)
        if not frame:
            print("Фрейм с расписанием не найден! Парсинг невозможен.")
            await browser.close()
            return {}
        await frame.wait_for_load_state('domcontentloaded')
        await asyncio.sleep(3)
        groups = await frame.evaluate('''() => {
            const select = document.querySelector('#groups');
            if (!select) return [];
            let result = [];
            for (let i = 0; i < select.options.length; i++) {
                let opt = select.options[i];
                if (opt.value && opt.value !== '0') {
                    result.push({id: opt.value, name: opt.text});
                }
            }
            return result;
        }''')
        print(f"Найдено групп: {len(groups)}")
        result = {}
        for group in groups:
            group_id = str(group['id'])
            group_name = group['name']
            url = f"https://coworking.tyuiu.ru/shs/mpn_t/mpn.php?action=group&union=0&sid=28705&gr={group_id}&year=2025&vr=1"
            department = "МПН"
            specialty = group_name.split('-')[0]
            result[group_id] = {
                "name": group_name,
                "url": url,
                "aliases": make_aliases(group_name),
                "department": department,
                "specialty": specialty
            }
        await browser.close()
        return result

def save_groups_full_py(groups_full: dict, filename: str = OUTPUT_FILE):
    """
    Сохраняет структуру groups_full МПН.py в виде python-файла.
    Это основной файл, который использует бот для поиска групп.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write("def make_aliases(name):\n    ... # см. оригинальную функцию\n\n")
        f.write("GROUPS_FULL = ")
        json_str = json.dumps(groups_full, ensure_ascii=False, indent=4)
        py_str = json_str.replace('true', 'True').replace('false', 'False').replace('null', 'None')
        py_str = py_str.replace('"', '\"')
        py_str = py_str.replace('\\"', '"')
        py_str = py_str.replace('    ', '    ')
        f.write(py_str)
        f.write("\n\n")
        f.write("def get_group_by_name(name):\n    ... # см. оригинальную функцию\n")

async def main():
    """
    Основная точка входа: парсит сайт и сохраняет результат в groups_full МПН.py.
    Просто запустите этот скрипт, чтобы обновить группы для бота.
    """
    print("Запуск автоматического обновления групп...")
    try:
        groups_full = await extract_groups_full()
        if not groups_full:
            print("Словарь групп пуст. Возможно, сайт недоступен или структура изменилась.")
            return
        save_groups_full_py(groups_full)
        print(f"Группы успешно обновлены и сохранены в {OUTPUT_FILE}")
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())

async def get_group_schedule_url(group_name):
    selection_url = "https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1301&Itemid=300"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    async with async_playwright() as p:
        print("Запускаем браузер...")
        browser = await p.chromium.launch(headless=False, slow_mo=100)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        try:
            print(f"Переходим на страницу выбора группы: {selection_url}")
            await page.goto(selection_url, timeout=60000)
            print("Ждем загрузки контента...")
            await asyncio.sleep(7)
            # Повторные попытки найти фрейм по url
            frame = None
            for attempt in range(7):
                frame = page.frame(url=re.compile(r"coworking\.tyuiu\.ru/shs/mpn_t/mpn\.php"))
                if frame:
                    print(f"Найден фрейм расписания: {frame.url}")
                    break
                print(f"Фрейм не найден, попытка {attempt+1}/7, жду...")
                await asyncio.sleep(2)
            if not frame:
                print("Фрейм с расписанием не найден")
                return None
            await frame.wait_for_load_state('domcontentloaded')
            await asyncio.sleep(3)
            print("Пробую выбрать группу и нажать кнопку через evaluate...")
            # Выполняем выбор группы и клик по кнопке через JS внутри фрейма
            result = await frame.evaluate('''(group_name) => {
                const select = document.querySelector('#groups');
                if (!select) return 'select not found';
                let found = false;
                for (let i = 0; i < select.options.length; i++) {
                    if (select.options[i].text.includes(group_name)) {
                        select.selectedIndex = i;
                        select.dispatchEvent(new Event('change', {bubbles:true}));
                        found = true;
                        break;
                    }
                }
                if (!found) return 'group not found';
                const btn = document.querySelector('button.butp');
                if (!btn) return 'button not found';
                btn.click();
                return 'ok';
            }''', group_name)
            print(f"Результат выполнения JS: {result}")
            if result != 'ok':
                print(f"Ошибка: {result}")
                return None
            await asyncio.sleep(7)
            frame_url = frame.url
            print(f"URL фрейма: {frame_url}")
            await page.screenshot(path="result_page.png")
            return frame_url
        except Exception as e:
            print(f"Ошибка при получении расписания: {e}")
            import traceback
            traceback.print_exc()
            return None
        finally:
            print("Закрываем браузер...")
            await context.close()
            await browser.close()

async def extract_group_ids():
    selection_url = "https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1301&Itemid=300"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    async with async_playwright() as p:
        print("Запускаем браузер...")
        browser = await p.chromium.launch(headless=False, slow_mo=100)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        try:
            print(f"Переходим на страницу выбора группы: {selection_url}")
            await page.goto(selection_url, timeout=60000)
            print("Ждем загрузки контента...")
            await asyncio.sleep(7)
            frame = None
            for attempt in range(7):
                frame = page.frame(url=re.compile(r"coworking\.tyuiu\.ru/shs/mpn_t/mpn\.php"))
                if frame:
                    print(f"Найден фрейм расписания: {frame.url}")
                    break
                print(f"Фрейм не найден, попытка {attempt+1}/7, жду...")
                await asyncio.sleep(2)
            if not frame:
                print("Фрейм с расписанием не найден")
                return None
            await frame.wait_for_load_state('domcontentloaded')
            await asyncio.sleep(3)
            print("Извлекаю ID и названия всех групп...")
            groups = await frame.evaluate('''() => {
                const select = document.querySelector('#groups');
                if (!select) return [];
                let result = [];
                for (let i = 0; i < select.options.length; i++) {
                    let opt = select.options[i];
                    if (opt.value && opt.value !== '0') {
                        result.push({id: opt.value, name: opt.text});
                    }
                }
                return result;
            }''')
            print("Список групп:")
            for group in groups:
                print(f"ID: {group['id']}, Название: {group['name']}")
            return groups
        except Exception as e:
            print(f"Ошибка при извлечении групп: {e}")
            import traceback
            traceback.print_exc()
            return None
        finally:
            print("Закрываем браузер...")
            await context.close()
            await browser.close()

async def get_schedule_url_for_group(group_name):
    selection_url = "https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1301&Itemid=300"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        try:
            await page.goto(selection_url, timeout=60000)
            await asyncio.sleep(5)
            frame = None
            for attempt in range(7):
                frame = page.frame(url=re.compile(r"coworking\.tyuiu\.ru/shs/mpn_t/mpn\.php"))
                if frame:
                    break
                await asyncio.sleep(2)
            if not frame:
                return None
            await frame.wait_for_load_state('domcontentloaded')
            await asyncio.sleep(2)
            result = await frame.evaluate('''(group_name) => {
                const select = document.querySelector('#groups');
                if (!select) return 'select not found';
                let found = false;
                for (let i = 0; i < select.options.length; i++) {
                    if (select.options[i].text.includes(group_name)) {
                        select.selectedIndex = i;
                        select.dispatchEvent(new Event('change', {bubbles:true}));
                        found = true;
                        break;
                    }
                }
                if (!found) return 'group not found';
                const btn = document.querySelector('button.butp');
                if (!btn) return 'button not found';
                btn.click();
                return 'ok';
            }''', group_name)
            if result != 'ok':
                return None
            await asyncio.sleep(5)
            return frame.url
        except Exception:
            return None
        finally:
            await context.close()
            await browser.close()

# Функция для красивого прогресс-бара
import sys

def print_progress_bar(iteration, total, prefix='', suffix='', length=40):
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

async def collect_all_group_urls():
    result = {}
    group_items = list(GROUPS.items())
    total = len(group_items)
    for idx, (group_id, group_name) in enumerate(group_items, 1):
        print_progress_bar(idx, total, prefix='Прогресс', suffix=f'{idx}/{total}', length=40)
        url = await get_schedule_url_for_group(group_name)
        if url:
            result[group_id] = {"name": group_name, "url": url}
        else:
            result[group_id] = {"name": group_name, "url": None}
    with open("groups_with_urls.py", "w", encoding="utf-8") as f:
        f.write("GROUPS_WITH_URLS = ")
        f.write(repr(result))
    print("\nРезультат сохранён в groups_with_urls.py")