import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import re
import json
from departments_config import departments

# --- НАСТРОЙКИ ---
SELECTION_URL = departments["НГО"]["selection_url"]  # URL страницы с выбором группы
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"  # User-Agent для браузера
OUTPUT_FILE = "groups_full НГО.py"  # Куда сохранять результат

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

async def extract_groups_full() -> dict:
    """
    Парсит сайт расписания и возвращает структуру для groups_full НГО.py.
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
                if f.url and f.url.startswith(departments["НГО"]["frame_url"]):
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
            url = f"https://coworking.tyuiu.ru/shs/ngo_t/ngo.php?action=group&union=0&sid=28703&gr={group_id}&year=2025&vr=1"
            department = "НГО"
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
    Сохраняет структуру groups_full НГО.py в виде python-файла.
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
    Основная точка входа: парсит сайт и сохраняет результат в groups_full НГО.py.
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