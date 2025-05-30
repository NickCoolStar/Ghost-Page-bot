"""
groups_dict.py — словарь с базовыми данными о группах
"""

def make_aliases(name):
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
    # Добавляем алиас с пробелами и без скобок/дефисов (например, 'СПт-23-(9)-1' -> 'Спт 23 9 1')
    spaced = name.replace('(', '').replace(')', '').replace('-', ' ')
    spaced = ' '.join(spaced.split())
    variants.extend([spaced, spaced.lower(), spaced.upper()])
    # Добавляем .title() для всех вариантов
    for v in list(variants):
        variants.append(v.title())
    aliases.update(variants)
    return list(aliases)

GROUPS = {
    "702": {"name": "ЗОт-22-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=702&year=2025&vr=1", "aliases": make_aliases("ЗОт-22-(9)-1"), "department": "СОНХ", "specialty": "ЗОт"},
    "703": {"name": "ЗОт-22-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=703&year=2025&vr=1", "aliases": make_aliases("ЗОт-22-(9)-2"), "department": "СОНХ", "specialty": "ЗОт"},
    "704": {"name": "ЗОт-22-(9)-3", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=704&year=2025&vr=1", "aliases": make_aliases("ЗОт-22-(9)-3"), "department": "СОНХ", "specialty": "ЗОт"},
    "789": {"name": "ЗУт-23-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=789&year=2025&vr=1", "aliases": make_aliases("ЗУт-23-(9)-1"), "department": "СОНХ", "specialty": "ЗУт"},
    "790": {"name": "ЗУт-23-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=790&year=2025&vr=1", "aliases": make_aliases("ЗУт-23-(9)-2"), "department": "СОНХ", "specialty": "ЗУт"},
    "791": {"name": "ЗУт-23-(9)-3", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=791&year=2025&vr=1", "aliases": make_aliases("ЗУт-23-(9)-3"), "department": "СОНХ", "specialty": "ЗУт"},
    "814": {"name": "ЗУт-24-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=814&year=2025&vr=1", "aliases": make_aliases("ЗУт-24-(9)-1"), "department": "СОНХ", "specialty": "ЗУт"},
    "815": {"name": "ЗУт-24-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=815&year=2025&vr=1", "aliases": make_aliases("ЗУт-24-(9)-2"), "department": "СОНХ", "specialty": "ЗУт"},
    "634": {"name": "ИСПт-21-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=634&year=2025&vr=1", "aliases": make_aliases("ИСПт-21-(9)-1"), "department": "СОНХ", "specialty": "ИСПт"},
    "705": {"name": "ИСПт-22-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=705&year=2025&vr=1", "aliases": make_aliases("ИСПт-22-(9)-1"), "department": "СОНХ", "specialty": "ИСПт"},
    "427": {"name": "ИСПт-22-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=427&year=2025&vr=1", "aliases": make_aliases("ИСПт-22-(9)-2"), "department": "СОНХ", "specialty": "ИСПт"},
    "706": {"name": "ИСПт-22-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=706&year=2025&vr=1", "aliases": make_aliases("ИСПт-22-(11)-1"), "department": "СОНХ", "specialty": "ИСПт"},
    "792": {"name": "ИСПт-23-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=792&year=2025&vr=1", "aliases": make_aliases("ИСПт-23-(9)-1"), "department": "СОНХ", "specialty": "ИСПт"},
    "793": {"name": "ИСПт-23-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=793&year=2025&vr=1", "aliases": make_aliases("ИСПт-23-(11)-1"), "department": "СОНХ", "specialty": "ИСПт"},
    "816": {"name": "ИСПт-24-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=816&year=2025&vr=1", "aliases": make_aliases("ИСПт-24-(9)-1"), "department": "СОНХ", "specialty": "ИСПт"},
    "817": {"name": "ИСПт-24-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=817&year=2025&vr=1", "aliases": make_aliases("ИСПт-24-(11)-1"), "department": "СОНХ", "specialty": "ИСПт"},
    "636": {"name": "РПКт-21-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=636&year=2025&vr=1", "aliases": make_aliases("РПКт-21-(9)-1"), "department": "СОНХ", "specialty": "РПКт"},
    "707": {"name": "РПКт-22-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=707&year=2025&vr=1", "aliases": make_aliases("РПКт-22-(9)-1"), "department": "СОНХ", "specialty": "РПКт"},
    "637": {"name": "СПт-21-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=637&year=2025&vr=1", "aliases": make_aliases("СПт-21-(9)-1"), "department": "СОНХ", "specialty": "СПт"},
    "708": {"name": "СПт-22-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=708&year=2025&vr=1", "aliases": make_aliases("СПт-22-(9)-1"), "department": "СОНХ", "specialty": "СПт"},
    "709": {"name": "СПт-22-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=709&year=2025&vr=1", "aliases": make_aliases("СПт-22-(11)-1"), "department": "СОНХ", "specialty": "СПт"},
    "794": {"name": "СПт-23-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=794&year=2025&vr=1", "aliases": make_aliases("СПт-23-(9)-1") + ["Спт 23 9 1"], "department": "СОНХ", "specialty": "СПт"},
    "795": {"name": "СПт-23-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=795&year=2025&vr=1", "aliases": make_aliases("СПт-23-(11)-1"), "department": "СОНХ", "specialty": "СПт"},
    "818": {"name": "СПт-24-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=818&year=2025&vr=1", "aliases": make_aliases("СПт-24-(9)-1"), "department": "СОНХ", "specialty": "СПт"},
    "819": {"name": "СПт-24-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=819&year=2025&vr=1", "aliases": make_aliases("СПт-24-(9)-2"), "department": "СОНХ", "specialty": "СПт"},
    "820": {"name": "СПт-24-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=820&year=2025&vr=1", "aliases": make_aliases("СПт-24-(11)-1"), "department": "СОНХ", "specialty": "СПт"},
    "796": {"name": "ЭБКт-23-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=796&year=2025&vr=1", "aliases": make_aliases("ЭБКт-23-(9)-1"), "department": "СОНХ", "specialty": "ЭБКт"},
    "821": {"name": "ЭБКт-24-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=821&year=2025&vr=1", "aliases": make_aliases("ЭБКт-24-(9)-1"), "department": "СОНХ", "specialty": "ЭБКт"},
    "822": {"name": "ЭБКт-24-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=822&year=2025&vr=1", "aliases": make_aliases("ЭБКт-24-(11)-1"), "department": "СОНХ", "specialty": "ЭБКт"},
    "571": {"name": "ЭГНт-20-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=571&year=2025&vr=1", "aliases": make_aliases("ЭГНт-20-(9)-1"), "department": "СОНХ", "specialty": "ЭГНт"},
    "572": {"name": "ЭГНт-20-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=572&year=2025&vr=1", "aliases": make_aliases("ЭГНт-20-(9)-2"), "department": "СОНХ", "specialty": "ЭГНт"},
    "639": {"name": "ЭГНт-21-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=639&year=2025&vr=1", "aliases": make_aliases("ЭГНт-21-(9)-1"), "department": "СОНХ", "specialty": "ЭГНт"},
    "640": {"name": "ЭГНт-21-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=640&year=2025&vr=1", "aliases": make_aliases("ЭГНт-21-(9)-2"), "department": "СОНХ", "specialty": "ЭГНт"},
    "710": {"name": "ЭГНт-22-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=710&year=2025&vr=1", "aliases": make_aliases("ЭГНт-22-(9)-1"), "department": "СОНХ", "specialty": "ЭГНт"},
    "711": {"name": "ЭГНт-22-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=711&year=2025&vr=1", "aliases": make_aliases("ЭГНт-22-(9)-2"), "department": "СОНХ", "specialty": "ЭГНт"},
    "712": {"name": "ЭГНт-22-(9)-3", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=712&year=2025&vr=1", "aliases": make_aliases("ЭГНт-22-(9)-3"), "department": "СОНХ", "specialty": "ЭГНт"},
    "713": {"name": "ЭГНт-22-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=713&year=2025&vr=1", "aliases": make_aliases("ЭГНт-22-(11)-1"), "department": "СОНХ", "specialty": "ЭГНт"},
    "797": {"name": "ЭГНт-23-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=797&year=2025&vr=1", "aliases": make_aliases("ЭГНт-23-(9)-1"), "department": "СОНХ", "specialty": "ЭГНт"},
    "798": {"name": "ЭГНт-23-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=798&year=2025&vr=1", "aliases": make_aliases("ЭГНт-23-(9)-2"), "department": "СОНХ", "specialty": "ЭГНт"},
    "799": {"name": "ЭГНт-23-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=799&year=2025&vr=1", "aliases": make_aliases("ЭГНт-23-(11)-1"), "department": "СОНХ", "specialty": "ЭГНт"},
    "823": {"name": "ЭГНт-24-(9)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=823&year=2025&vr=1", "aliases": make_aliases("ЭГНт-24-(9)-1"), "department": "СОНХ", "specialty": "ЭГНт"},
    "824": {"name": "ЭГНт-24-(9)-2", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=824&year=2025&vr=1", "aliases": make_aliases("ЭГНт-24-(9)-2"), "department": "СОНХ", "specialty": "ЭГНт"},
    "825": {"name": "ЭГНт-24-(11)-1", "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=825&year=2025&vr=1", "aliases": make_aliases("ЭГНт-24-(11)-1"), "department": "СОНХ", "specialty": "ЭГНт"},
}
  # Пустой словарь, так как мы будем получать данные с сайта 

# --- НАСТРОЙКИ ---
SELECTION_URL = "https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1302&Itemid=302"  # Обновленный URL
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OUTPUT_FILE = "groups_full.py"

if __name__ == "__main__":
    asyncio.run(main()) 