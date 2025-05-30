"""
groups_full.py — основной источник данных о группах для Telegram-бота

Использование:
    from groups_full import GROUPS_FULL, get_group_by_name

GROUPS_FULL — словарь с данными о группах:
    ключ — строковый ID группы
    значение — словарь с полями:
        name — название группы
        url — ссылка на расписание
        aliases — список альтернативных названий
        department — отделение
        specialty — специальность

get_group_by_name(name) — функция для поиска группы по названию или алиасу

Файл автоматически обновляется скриптом parse_groups.py
"""

from bot.parsers.groups_fulls.groups_full_АиЭС import GROUPS_FULL as AIES
from bot.parsers.groups_fulls.groups_full_МПН import GROUPS_FULL as MPN
from bot.parsers.groups_fulls.groups_full_НГО import GROUPS_FULL as NGO
from bot.parsers.groups_fulls.groups_full_СОНХ import GROUPS_FULL as SONH
from bot.parsers.groups_fulls.groups_full_ПО import GROUPS_FULL as PO

from bot.parsers.groups_fulls.groups_full_АиЭС import make_aliases

all_groups = {}
for d in (AIES, MPN, NGO, SONH, PO):
    for group_id, group in d.items():
        all_groups[group_id] = {
            "name": group["name"],
            "url": group["url"],
            "aliases": f'make_aliases("{group["name"]}")',
            "department": group["department"],
            "specialty": group["specialty"]
        }

with open("bot/groups_full.py", "w", encoding="utf-8") as f:
    f.write('from bot.parsers.groups_fulls.groups_full_АиЭС import make_aliases\n\n')
    f.write('GROUPS_FULL = {\n')
    for group_id, group in all_groups.items():
        f.write(f'    "{group_id}": {{\n')
        f.write(f'        "name": "{group["name"]}",\n')
        f.write(f'        "url": "{group["url"]}",\n')
        f.write(f'        "aliases": {group["aliases"]},\n')
        f.write(f'        "department": "{group["department"]}",\n')
        f.write(f'        "specialty": "{group["specialty"]}"\n')
        f.write('    },\n')
    f.write('}\n\n')
    f.write('def get_group_by_name(name: str):\n')
    f.write('    for group_id, group_data in GROUPS_FULL.items():\n')
    f.write('        if name == group_data["name"]:\n')
    f.write('            return group_data["name"], group_data\n')
    f.write('    for group_id, group_data in GROUPS_FULL.items():\n')
    f.write('        if name in group_data.get("aliases", []):\n')
    f.write('            return group_data["name"], group_data\n')
    f.write('    return None, None\n') 