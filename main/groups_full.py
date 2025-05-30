from bot.parsers.groups_fulls.groups_full_АиЭС import make_aliases

def make_aliases(name):
    """Generate various aliases for a group name."""
    aliases = []
    
    # Original name
    aliases.append(name)
    
    # Replace hyphens with spaces
    aliases.append(name.replace("-", " "))
    
    # Remove parentheses
    aliases.append(name.replace("(", "").replace(")", ""))
    
    # Remove parentheses and replace hyphens with spaces
    aliases.append(name.replace("(", "").replace(")", "").replace("-", " "))
    
    # Uppercase version
    aliases.append(name.upper())
    
    # Lowercase version
    aliases.append(name.lower())
    
    # Title case version
    aliases.append(name.title())
    
    # Variants with different case combinations
    parts = name.split("-")
    if len(parts) >= 2:
        specialty = parts[0]
        year = parts[1]
        group = parts[2] if len(parts) > 2 else ""
        
        # Different case combinations for specialty
        aliases.append(f"{specialty.upper()}-{year}-{group}")
        aliases.append(f"{specialty.lower()}-{year}-{group}")
        aliases.append(f"{specialty.title()}-{year}-{group}")
        
        # With spaces instead of hyphens
        aliases.append(f"{specialty.upper()} {year} {group}")
        aliases.append(f"{specialty.lower()} {year} {group}")
        aliases.append(f"{specialty.title()} {year} {group}")
        
        # Without parentheses
        clean_group = group.replace("(", "").replace(")", "")
        aliases.append(f"{specialty.upper()}-{year}-{clean_group}")
        aliases.append(f"{specialty.lower()}-{year}-{clean_group}")
        aliases.append(f"{specialty.title()}-{year}-{clean_group}")
        
        # Without parentheses and with spaces
        aliases.append(f"{specialty.upper()} {year} {clean_group}")
        aliases.append(f"{specialty.lower()} {year} {clean_group}")
        aliases.append(f"{specialty.title()} {year} {clean_group}")
        
        # Additional variants for СПт groups
        if specialty == "СПт":
            # Variants with "Спт" instead of "СПт"
            aliases.append(f"Спт-{year}-{group}")
            aliases.append(f"Спт {year} {group}")
            aliases.append(f"Спт-{year}-{clean_group}")
            aliases.append(f"Спт {year} {clean_group}")
            
            # Variants with "спт" instead of "СПт"
            aliases.append(f"спт-{year}-{group}")
            aliases.append(f"спт {year} {group}")
            aliases.append(f"спт-{year}-{clean_group}")
            aliases.append(f"спт {year} {clean_group}")
    
    # Remove duplicates and return
    return list(dict.fromkeys(aliases))

GROUPS_FULL = {
    "726": {
        "name": "КИПр-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=726&year=2025&vr=1",
        "aliases": make_aliases("КИПр-22-(9)-1"),
        "department": "АиЭС",
        "specialty": "КИПр"
    },
    "768": {
        "name": "КИПр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=768&year=2025&vr=1",
        "aliases": make_aliases("КИПр-23-(9)-1"),
        "department": "АиЭС",
        "specialty": "КИПр"
    },
    "842": {
        "name": "КИПр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=842&year=2025&vr=1",
        "aliases": make_aliases("КИПр-24-(9)-1"),
        "department": "АиЭС",
        "specialty": "КИПр"
    },
    "843": {
        "name": "КИПр-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=843&year=2025&vr=1",
        "aliases": make_aliases("КИПр-24-(11)-1"),
        "department": "АиЭС",
        "specialty": "КИПр"
    },
    "672": {
        "name": "КСт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=672&year=2025&vr=1",
        "aliases": make_aliases("КСт-21-(9)-1"),
        "department": "АиЭС",
        "specialty": "КСт"
    },
    "728": {
        "name": "КСт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=728&year=2025&vr=1",
        "aliases": make_aliases("КСт-22-(9)-1"),
        "department": "АиЭС",
        "specialty": "КСт"
    },
    "729": {
        "name": "КСт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=729&year=2025&vr=1",
        "aliases": make_aliases("КСт-22-(11)-1"),
        "department": "АиЭС",
        "specialty": "КСт"
    },
    "769": {
        "name": "КСт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=769&year=2025&vr=1",
        "aliases": make_aliases("КСт-23-(9)-1"),
        "department": "АиЭС",
        "specialty": "КСт"
    },
    "770": {
        "name": "КСт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=770&year=2025&vr=1",
        "aliases": make_aliases("КСт-23-(9)-2"),
        "department": "АиЭС",
        "specialty": "КСт"
    },
    "775": {
        "name": "КСт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=775&year=2025&vr=1",
        "aliases": make_aliases("КСт-23-(11)-1"),
        "department": "АиЭС",
        "specialty": "КСт"
    },
    "844": {
        "name": "КСт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=844&year=2025&vr=1",
        "aliases": make_aliases("КСт-24-(9)-1"),
        "department": "АиЭС",
        "specialty": "КСт"
    },
    "845": {
        "name": "КСт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=845&year=2025&vr=1",
        "aliases": make_aliases("КСт-24-(9)-2"),
        "department": "АиЭС",
        "specialty": "КСт"
    },
    "846": {
        "name": "КСт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=846&year=2025&vr=1",
        "aliases": make_aliases("КСт-24-(11)-1"),
        "department": "АиЭС",
        "specialty": "КСт"
    },
    "838": {
        "name": "МСр-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=838&year=2025&vr=1",
        "aliases": make_aliases("МСр-24-(11)-1"),
        "department": "АиЭС",
        "specialty": "МСр"
    },
    "724": {
        "name": "ОСр-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=724&year=2025&vr=1",
        "aliases": make_aliases("ОСр-22-(9)-1"),
        "department": "АиЭС",
        "specialty": "ОСр"
    },
    "767": {
        "name": "ОСр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=767&year=2025&vr=1",
        "aliases": make_aliases("ОСр-23-(9)-1"),
        "department": "АиЭС",
        "specialty": "ОСр"
    },
    "839": {
        "name": "ОСр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=839&year=2025&vr=1",
        "aliases": make_aliases("ОСр-24-(9)-1"),
        "department": "АиЭС",
        "specialty": "ОСр"
    },
    "774": {
        "name": "ОТПт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=774&year=2025&vr=1",
        "aliases": make_aliases("ОТПт-23-(9)-1"),
        "department": "АиЭС",
        "specialty": "ОТПт"
    },
    "676": {
        "name": "РРТт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=676&year=2025&vr=1",
        "aliases": make_aliases("РРТт-21-(9)-1"),
        "department": "АиЭС",
        "specialty": "РРТт"
    },
    "730": {
        "name": "РРТт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=730&year=2025&vr=1",
        "aliases": make_aliases("РРТт-22-(9)-1"),
        "department": "АиЭС",
        "specialty": "РРТт"
    },
    "771": {
        "name": "СРТт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=771&year=2025&vr=1",
        "aliases": make_aliases("СРТт-23-(9)-1"),
        "department": "АиЭС",
        "specialty": "СРТт"
    },
    "847": {
        "name": "СРТт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=847&year=2025&vr=1",
        "aliases": make_aliases("СРТт-24-(9)-1"),
        "department": "АиЭС",
        "specialty": "СРТт"
    },
    "674": {
        "name": "ТЭОт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=674&year=2025&vr=1",
        "aliases": make_aliases("ТЭОт-21-(9)-1"),
        "department": "АиЭС",
        "specialty": "ТЭОт"
    },
    "675": {
        "name": "ТЭОт-21-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=675&year=2025&vr=1",
        "aliases": make_aliases("ТЭОт-21-(9)-2"),
        "department": "АиЭС",
        "specialty": "ТЭОт"
    },
    "731": {
        "name": "ТЭОт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=731&year=2025&vr=1",
        "aliases": make_aliases("ТЭОт-22-(9)-1"),
        "department": "АиЭС",
        "specialty": "ТЭОт"
    },
    "732": {
        "name": "ТЭОт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=732&year=2025&vr=1",
        "aliases": make_aliases("ТЭОт-22-(9)-2"),
        "department": "АиЭС",
        "specialty": "ТЭОт"
    },
    "733": {
        "name": "ТЭОт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=733&year=2025&vr=1",
        "aliases": make_aliases("ТЭОт-22-(11)-1"),
        "department": "АиЭС",
        "specialty": "ТЭОт"
    },
    "772": {
        "name": "ТЭОт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=772&year=2025&vr=1",
        "aliases": make_aliases("ТЭОт-23-(9)-1"),
        "department": "АиЭС",
        "specialty": "ТЭОт"
    },
    "773": {
        "name": "ТЭОт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=773&year=2025&vr=1",
        "aliases": make_aliases("ТЭОт-23-(9)-2"),
        "department": "АиЭС",
        "specialty": "ТЭОт"
    },
    "776": {
        "name": "ТЭОт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=776&year=2025&vr=1",
        "aliases": make_aliases("ТЭОт-23-(11)-1"),
        "department": "АиЭС",
        "specialty": "ТЭОт"
    },
    "848": {
        "name": "ЭОт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=848&year=2025&vr=1",
        "aliases": make_aliases("ЭОт-24-(9)-1"),
        "department": "АиЭС",
        "specialty": "ЭОт"
    },
    "849": {
        "name": "ЭОт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=849&year=2025&vr=1",
        "aliases": make_aliases("ЭОт-24-(9)-2"),
        "department": "АиЭС",
        "specialty": "ЭОт"
    },
    "850": {
        "name": "ЭОт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=850&year=2025&vr=1",
        "aliases": make_aliases("ЭОт-24-(11)-1"),
        "department": "АиЭС",
        "specialty": "ЭОт"
    },
    "725": {
        "name": "ЭРЭр-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=725&year=2025&vr=1",
        "aliases": make_aliases("ЭРЭр-22-(9)-1"),
        "department": "АиЭС",
        "specialty": "ЭРЭр"
    },
    "766": {
        "name": "ЭРЭр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=766&year=2025&vr=1",
        "aliases": make_aliases("ЭРЭр-23-(9)-1"),
        "department": "АиЭС",
        "specialty": "ЭРЭр"
    },
    "840": {
        "name": "ЭРЭр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=840&year=2025&vr=1",
        "aliases": make_aliases("ЭРЭр-24-(9)-1"),
        "department": "АиЭС",
        "specialty": "ЭРЭр"
    },
    "841": {
        "name": "ЭРЭр-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=841&year=2025&vr=1",
        "aliases": make_aliases("ЭРЭр-24-(11)-1"),
        "department": "АиЭС",
        "specialty": "ЭРЭр"
    },
    "837": {
        "name": "ЭСр-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=837&year=2025&vr=1",
        "aliases": make_aliases("ЭСр-24-(11)-1"),
        "department": "АиЭС",
        "specialty": "ЭСр"
    },
    "667": {
        "name": "МТОт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=667&year=2025&vr=1",
        "aliases": make_aliases("МТОт-21-(9)-1"),
        "department": "МПН",
        "specialty": "МТОт"
    },
    "742": {
        "name": "МТОт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=742&year=2025&vr=1",
        "aliases": make_aliases("МТОт-22-(9)-1"),
        "department": "МПН",
        "specialty": "МТОт"
    },
    "664": {
        "name": "МТОт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=664&year=2025&vr=1",
        "aliases": make_aliases("МТОт-22-(9)-2"),
        "department": "МПН",
        "specialty": "МТОт"
    },
    "739": {
        "name": "МТОт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=739&year=2025&vr=1",
        "aliases": make_aliases("МТОт-22-(11)-1"),
        "department": "МПН",
        "specialty": "МТОт"
    },
    "782": {
        "name": "МТОт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=782&year=2025&vr=1",
        "aliases": make_aliases("МТОт-23-(9)-1"),
        "department": "МПН",
        "specialty": "МТОт"
    },
    "784": {
        "name": "МТОт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=784&year=2025&vr=1",
        "aliases": make_aliases("МТОт-23-(11)-1"),
        "department": "МПН",
        "specialty": "МТОт"
    },
    "858": {
        "name": "МТОт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=858&year=2025&vr=1",
        "aliases": make_aliases("МТОт-24-(9)-1"),
        "department": "МПН",
        "specialty": "МТОт"
    },
    "859": {
        "name": "МТОт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=859&year=2025&vr=1",
        "aliases": make_aliases("МТОт-24-(11)-1"),
        "department": "МПН",
        "specialty": "МТОт"
    },
    "851": {
        "name": "ОМСтр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=851&year=2025&vr=1",
        "aliases": make_aliases("ОМСтр-24-(9)-1"),
        "department": "МПН",
        "specialty": "ОМСтр"
    },
    "852": {
        "name": "ОМСтр-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=852&year=2025&vr=1",
        "aliases": make_aliases("ОМСтр-24-(11)-1"),
        "department": "МПН",
        "specialty": "ОМСтр"
    },
    "853": {
        "name": "ОМСфр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=853&year=2025&vr=1",
        "aliases": make_aliases("ОМСфр-24-(9)-1"),
        "department": "МПН",
        "specialty": "ОМСфр"
    },
    "854": {
        "name": "ОМСфр-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=854&year=2025&vr=1",
        "aliases": make_aliases("ОМСфр-24-(11)-1"),
        "department": "МПН",
        "specialty": "ОМСфр"
    },
    "860": {
        "name": "ПНГт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=860&year=2025&vr=1",
        "aliases": make_aliases("ПНГт-24-(9)-1"),
        "department": "МПН",
        "specialty": "ПНГт"
    },
    "665": {
        "name": "ТМт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=665&year=2025&vr=1",
        "aliases": make_aliases("ТМт-21-(9)-1"),
        "department": "МПН",
        "specialty": "ТМт"
    },
    "666": {
        "name": "ТМт-21-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=666&year=2025&vr=1",
        "aliases": make_aliases("ТМт-21-(9)-2"),
        "department": "МПН",
        "specialty": "ТМт"
    },
    "737": {
        "name": "ТМт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=737&year=2025&vr=1",
        "aliases": make_aliases("ТМт-22-(9)-1"),
        "department": "МПН",
        "specialty": "ТМт"
    },
    "738": {
        "name": "ТМт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=738&year=2025&vr=1",
        "aliases": make_aliases("ТМт-22-(9)-2"),
        "department": "МПН",
        "specialty": "ТМт"
    },
    "785": {
        "name": "ТМт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=785&year=2025&vr=1",
        "aliases": make_aliases("ТМт-23-(9)-1"),
        "department": "МПН",
        "specialty": "ТМт"
    },
    "786": {
        "name": "ТМт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=786&year=2025&vr=1",
        "aliases": make_aliases("ТМт-23-(9)-2"),
        "department": "МПН",
        "specialty": "ТМт"
    },
    "856": {
        "name": "ТМт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=856&year=2025&vr=1",
        "aliases": make_aliases("ТМт-24-(9)-1"),
        "department": "МПН",
        "specialty": "ТМт"
    },
    "857": {
        "name": "ТМт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=857&year=2025&vr=1",
        "aliases": make_aliases("ТМт-24-(9)-2"),
        "department": "МПН",
        "specialty": "ТМт"
    },
    "777": {
        "name": "ТСр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=777&year=2025&vr=1",
        "aliases": make_aliases("ТСр-23-(9)-1"),
        "department": "МПН",
        "specialty": "ТСр"
    },
    "663": {
        "name": "ТТОт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=663&year=2025&vr=1",
        "aliases": make_aliases("ТТОт-21-(9)-1"),
        "department": "МПН",
        "specialty": "ТТОт"
    },
    "736": {
        "name": "ТТОт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=736&year=2025&vr=1",
        "aliases": make_aliases("ТТОт-22-(9)-1"),
        "department": "МПН",
        "specialty": "ТТОт"
    },
    "781": {
        "name": "ТТОт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=781&year=2025&vr=1",
        "aliases": make_aliases("ТТОт-23-(9)-1"),
        "department": "МПН",
        "specialty": "ТТОт"
    },
    "855": {
        "name": "ТТОт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=855&year=2025&vr=1",
        "aliases": make_aliases("ТТОт-24-(9)-1"),
        "department": "МПН",
        "specialty": "ТТОт"
    },
    "861": {
        "name": "УКПт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=861&year=2025&vr=1",
        "aliases": make_aliases("УКПт-24-(9)-1"),
        "department": "МПН",
        "specialty": "УКПт"
    },
    "779": {
        "name": "ФСр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=779&year=2025&vr=1",
        "aliases": make_aliases("ФСр-23-(9)-1"),
        "department": "МПН",
        "specialty": "ФСр"
    },
    "700": {
        "name": "ПНГт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=700&year=2025&vr=1",
        "aliases": make_aliases("ПНГт-21-(9)-1"),
        "department": "МПН",
        "specialty": "ПНГт"
    },
    "740": {
        "name": "ПНГт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=740&year=2025&vr=1",
        "aliases": make_aliases("ПНГт-22-(9)-1"),
        "department": "МПН",
        "specialty": "ПНГт"
    },
    "787": {
        "name": "ПНГт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=787&year=2025&vr=1",
        "aliases": make_aliases("ПНГт-23-(9)-1"),
        "department": "МПН",
        "specialty": "ПНГт"
    },
    "747": {
        "name": "ПНГт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=747&year=2025&vr=1",
        "aliases": make_aliases("ПНГт-23-(11)-1"),
        "department": "МПН",
        "specialty": "ПНГт"
    },
    "862": {
        "name": "ПНГт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=862&year=2025&vr=1",
        "aliases": make_aliases("ПНГт-24-(11)-1"),
        "department": "МПН",
        "specialty": "ПНГт"
    },
    "701": {
        "name": "УКПт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=701&year=2025&vr=1",
        "aliases": make_aliases("УКПт-21-(9)-1"),
        "department": "МПН",
        "specialty": "УКПт"
    },
    "741": {
        "name": "УКПт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=741&year=2025&vr=1",
        "aliases": make_aliases("УКПт-22-(9)-1"),
        "department": "МПН",
        "specialty": "УКПт"
    },
    "788": {
        "name": "УКПт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=788&year=2025&vr=1",
        "aliases": make_aliases("УКПт-23-(9)-1"),
        "department": "МПН",
        "specialty": "УКПт"
    },
    "746": {
        "name": "УКПт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=746&year=2025&vr=1",
        "aliases": make_aliases("УКПт-23-(11)-1"),
        "department": "МПН",
        "specialty": "УКПт"
    },
    "863": {
        "name": "УКПт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28705&gr=863&year=2025&vr=1",
        "aliases": make_aliases("УКПт-24-(11)-1"),
        "department": "МПН",
        "specialty": "УКПт"
    },
    "686": {
        "name": "БСр-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=686&year=2025&vr=1",
        "aliases": make_aliases("БСр-22-(9)-1"),
        "department": "НГО",
        "specialty": "БСр"
    },
    "758": {
        "name": "БСр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=758&year=2025&vr=1",
        "aliases": make_aliases("БСр-23-(9)-1"),
        "department": "НГО",
        "specialty": "БСр"
    },
    "752": {
        "name": "БСр-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=752&year=2025&vr=1",
        "aliases": make_aliases("БСр-23-(11)-1"),
        "department": "НГО",
        "specialty": "БСр"
    },
    "868": {
        "name": "БСр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=868&year=2025&vr=1",
        "aliases": make_aliases("БСр-24-(9)-1"),
        "department": "НГО",
        "specialty": "БСр"
    },
    "869": {
        "name": "БСр-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=869&year=2025&vr=1",
        "aliases": make_aliases("БСр-24-(11)-1"),
        "department": "НГО",
        "specialty": "БСр"
    },
    "661": {
        "name": "БСт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=661&year=2025&vr=1",
        "aliases": make_aliases("БСт-21-(9)-1"),
        "department": "НГО",
        "specialty": "БСт"
    },
    "692": {
        "name": "БСт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=692&year=2025&vr=1",
        "aliases": make_aliases("БСт-22-(9)-1"),
        "department": "НГО",
        "specialty": "БСт"
    },
    "691": {
        "name": "БСт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=691&year=2025&vr=1",
        "aliases": make_aliases("БСт-22-(11)-1"),
        "department": "НГО",
        "specialty": "БСт"
    },
    "755": {
        "name": "БСт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=755&year=2025&vr=1",
        "aliases": make_aliases("БСт-23-(9)-1"),
        "department": "НГО",
        "specialty": "БСт"
    },
    "748": {
        "name": "БСт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=748&year=2025&vr=1",
        "aliases": make_aliases("БСт-23-(11)-1"),
        "department": "НГО",
        "specialty": "БСт"
    },
    "877": {
        "name": "БСт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=877&year=2025&vr=1",
        "aliases": make_aliases("БСт-24-(9)-1"),
        "department": "НГО",
        "specialty": "БСт"
    },
    "878": {
        "name": "БСт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=878&year=2025&vr=1",
        "aliases": make_aliases("БСт-24-(11)-1"),
        "department": "НГО",
        "specialty": "БСт"
    },
    "879": {
        "name": "БСт-24-(11)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=879&year=2025&vr=1",
        "aliases": make_aliases("БСт-24-(11)-2"),
        "department": "НГО",
        "specialty": "БСт"
    },
    "698": {
        "name": "ГНГт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=698&year=2025&vr=1",
        "aliases": make_aliases("ГНГт-22-(11)-1"),
        "department": "НГО",
        "specialty": "ГНГт"
    },
    "749": {
        "name": "ГНГт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=749&year=2025&vr=1",
        "aliases": make_aliases("ГНГт-23-(11)-1"),
        "department": "НГО",
        "specialty": "ГНГт"
    },
    "880": {
        "name": "ГНГт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=880&year=2025&vr=1",
        "aliases": make_aliases("ГНГт-24-(9)-1"),
        "department": "НГО",
        "specialty": "ГНГт"
    },
    "881": {
        "name": "ГНГт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=881&year=2025&vr=1",
        "aliases": make_aliases("ГНГт-24-(11)-1"),
        "department": "НГО",
        "specialty": "ГНГт"
    },
    "687": {
        "name": "МБр-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=687&year=2025&vr=1",
        "aliases": make_aliases("МБр-22-(9)-1"),
        "department": "НГО",
        "specialty": "МБр"
    },
    "759": {
        "name": "МБр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=759&year=2025&vr=1",
        "aliases": make_aliases("МБр-23-(9)-1"),
        "department": "НГО",
        "specialty": "МБр"
    },
    "870": {
        "name": "МБр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=870&year=2025&vr=1",
        "aliases": make_aliases("МБр-24-(9)-1"),
        "department": "НГО",
        "specialty": "МБр"
    },
    "871": {
        "name": "МБр-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=871&year=2025&vr=1",
        "aliases": make_aliases("МБр-24-(11)-1"),
        "department": "НГО",
        "specialty": "МБр"
    },
    "688": {
        "name": "МТНр-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=688&year=2025&vr=1",
        "aliases": make_aliases("МТНр-22-(9)-1"),
        "department": "НГО",
        "specialty": "МТНр"
    },
    "760": {
        "name": "МТНр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=760&year=2025&vr=1",
        "aliases": make_aliases("МТНр-23-(9)-1"),
        "department": "НГО",
        "specialty": "МТНр"
    },
    "864": {
        "name": "МТНр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=864&year=2025&vr=1",
        "aliases": make_aliases("МТНр-24-(9)-1"),
        "department": "НГО",
        "specialty": "МТНр"
    },
    "865": {
        "name": "МТНр-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=865&year=2025&vr=1",
        "aliases": make_aliases("МТНр-24-(11)-1"),
        "department": "НГО",
        "specialty": "МТНр"
    },
    "689": {
        "name": "НГСр-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=689&year=2025&vr=1",
        "aliases": make_aliases("НГСр-22-(9)-1"),
        "department": "НГО",
        "specialty": "НГСр"
    },
    "761": {
        "name": "НГСр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=761&year=2025&vr=1",
        "aliases": make_aliases("НГСр-23-(9)-1"),
        "department": "НГО",
        "specialty": "НГСр"
    },
    "866": {
        "name": "НГСр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=866&year=2025&vr=1",
        "aliases": make_aliases("НГСр-24-(9)-1"),
        "department": "НГО",
        "specialty": "НГСр"
    },
    "657": {
        "name": "НРт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=657&year=2025&vr=1",
        "aliases": make_aliases("НРт-21-(9)-1"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "658": {
        "name": "НРт-21-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=658&year=2025&vr=1",
        "aliases": make_aliases("НРт-21-(9)-2"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "695": {
        "name": "НРт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=695&year=2025&vr=1",
        "aliases": make_aliases("НРт-22-(9)-1"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "696": {
        "name": "НРт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=696&year=2025&vr=1",
        "aliases": make_aliases("НРт-22-(9)-2"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "697": {
        "name": "НРт-22-(9)-3",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=697&year=2025&vr=1",
        "aliases": make_aliases("НРт-22-(9)-3"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "745": {
        "name": "НРт-22-(9)-4",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=745&year=2025&vr=1",
        "aliases": make_aliases("НРт-22-(9)-4"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "693": {
        "name": "НРт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=693&year=2025&vr=1",
        "aliases": make_aliases("НРт-22-(11)-1"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "694": {
        "name": "НРт-22-(11)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=694&year=2025&vr=1",
        "aliases": make_aliases("НРт-22-(11)-2"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "756": {
        "name": "НРт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=756&year=2025&vr=1",
        "aliases": make_aliases("НРт-23-(9)-1"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "757": {
        "name": "НРт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=757&year=2025&vr=1",
        "aliases": make_aliases("НРт-23-(9)-2"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "750": {
        "name": "НРт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=750&year=2025&vr=1",
        "aliases": make_aliases("НРт-23-(11)-1"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "751": {
        "name": "НРт-23-(11)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=751&year=2025&vr=1",
        "aliases": make_aliases("НРт-23-(11)-2"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "872": {
        "name": "НРт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=872&year=2025&vr=1",
        "aliases": make_aliases("НРт-24-(9)-1"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "873": {
        "name": "НРт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=873&year=2025&vr=1",
        "aliases": make_aliases("НРт-24-(9)-2"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "874": {
        "name": "НРт-24-(9)-3",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=874&year=2025&vr=1",
        "aliases": make_aliases("НРт-24-(9)-3"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "875": {
        "name": "НРт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=875&year=2025&vr=1",
        "aliases": make_aliases("НРт-24-(11)-1"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "876": {
        "name": "НРт-24-(11)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=876&year=2025&vr=1",
        "aliases": make_aliases("НРт-24-(11)-2"),
        "department": "НГО",
        "specialty": "НРт"
    },
    "690": {
        "name": "ОРСр-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=690&year=2025&vr=1",
        "aliases": make_aliases("ОРСр-22-(9)-1"),
        "department": "НГО",
        "specialty": "ОРСр"
    },
    "762": {
        "name": "ОРСр-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=762&year=2025&vr=1",
        "aliases": make_aliases("ОРСр-23-(9)-1"),
        "department": "НГО",
        "specialty": "ОРСр"
    },
    "867": {
        "name": "ОРСр-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=867&year=2025&vr=1",
        "aliases": make_aliases("ОРСр-24-(9)-1"),
        "department": "НГО",
        "specialty": "ОРСр"
    },
    "702": {
        "name": "ЗОт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=702&year=2025&vr=1",
        "aliases": make_aliases("ЗОт-22-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЗОт"
    },
    "703": {
        "name": "ЗОт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=703&year=2025&vr=1",
        "aliases": make_aliases("ЗОт-22-(9)-2"),
        "department": "СОНХ",
        "specialty": "ЗОт"
    },
    "704": {
        "name": "ЗОт-22-(9)-3",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=704&year=2025&vr=1",
        "aliases": make_aliases("ЗОт-22-(9)-3"),
        "department": "СОНХ",
        "specialty": "ЗОт"
    },
    "789": {
        "name": "ЗУт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=789&year=2025&vr=1",
        "aliases": make_aliases("ЗУт-23-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЗУт"
    },
    "790": {
        "name": "ЗУт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=790&year=2025&vr=1",
        "aliases": make_aliases("ЗУт-23-(9)-2"),
        "department": "СОНХ",
        "specialty": "ЗУт"
    },
    "791": {
        "name": "ЗУт-23-(9)-3",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=791&year=2025&vr=1",
        "aliases": make_aliases("ЗУт-23-(9)-3"),
        "department": "СОНХ",
        "specialty": "ЗУт"
    },
    "814": {
        "name": "ЗУт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=814&year=2025&vr=1",
        "aliases": make_aliases("ЗУт-24-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЗУт"
    },
    "815": {
        "name": "ЗУт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=815&year=2025&vr=1",
        "aliases": make_aliases("ЗУт-24-(9)-2"),
        "department": "СОНХ",
        "specialty": "ЗУт"
    },
    "634": {
        "name": "ИСПт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=634&year=2025&vr=1",
        "aliases": make_aliases("ИСПт-21-(9)-1"),
        "department": "СОНХ",
        "specialty": "ИСПт"
    },
    "705": {
        "name": "ИСПт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=705&year=2025&vr=1",
        "aliases": make_aliases("ИСПт-22-(9)-1"),
        "department": "СОНХ",
        "specialty": "ИСПт"
    },
    "427": {
        "name": "ИСПт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=427&year=2025&vr=1",
        "aliases": make_aliases("ИСПт-22-(9)-2"),
        "department": "СОНХ",
        "specialty": "ИСПт"
    },
    "706": {
        "name": "ИСПт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=706&year=2025&vr=1",
        "aliases": make_aliases("ИСПт-22-(11)-1"),
        "department": "СОНХ",
        "specialty": "ИСПт"
    },
    "792": {
        "name": "ИСПт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=792&year=2025&vr=1",
        "aliases": make_aliases("ИСПт-23-(9)-1"),
        "department": "СОНХ",
        "specialty": "ИСПт"
    },
    "793": {
        "name": "ИСПт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=793&year=2025&vr=1",
        "aliases": make_aliases("ИСПт-23-(11)-1"),
        "department": "СОНХ",
        "specialty": "ИСПт"
    },
    "816": {
        "name": "ИСПт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=816&year=2025&vr=1",
        "aliases": make_aliases("ИСПт-24-(9)-1"),
        "department": "СОНХ",
        "specialty": "ИСПт"
    },
    "817": {
        "name": "ИСПт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=817&year=2025&vr=1",
        "aliases": make_aliases("ИСПт-24-(11)-1"),
        "department": "СОНХ",
        "specialty": "ИСПт"
    },
    "636": {
        "name": "РПКт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=636&year=2025&vr=1",
        "aliases": make_aliases("РПКт-21-(9)-1"),
        "department": "СОНХ",
        "specialty": "РПКт"
    },
    "707": {
        "name": "РПКт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=707&year=2025&vr=1",
        "aliases": make_aliases("РПКт-22-(9)-1"),
        "department": "СОНХ",
        "specialty": "РПКт"
    },
    "796": {
        "name": "ЭБКт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=796&year=2025&vr=1",
        "aliases": make_aliases("ЭБКт-23-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЭБКт"
    },
    "821": {
        "name": "ЭБКт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=821&year=2025&vr=1",
        "aliases": make_aliases("ЭБКт-24-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЭБКт"
    },
    "822": {
        "name": "ЭБКт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=822&year=2025&vr=1",
        "aliases": make_aliases("ЭБКт-24-(11)-1"),
        "department": "СОНХ",
        "specialty": "ЭБКт"
    },
    "571": {
        "name": "ЭГНт-20-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=571&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-20-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "572": {
        "name": "ЭГНт-20-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=572&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-20-(9)-2"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "639": {
        "name": "ЭГНт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=639&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-21-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "640": {
        "name": "ЭГНт-21-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=640&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-21-(9)-2"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "710": {
        "name": "ЭГНт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=710&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-22-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "711": {
        "name": "ЭГНт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=711&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-22-(9)-2"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "712": {
        "name": "ЭГНт-22-(9)-3",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=712&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-22-(9)-3"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "713": {
        "name": "ЭГНт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/sonh_po_t/sonh_po.php?action=group&union=0&sid=28702&gr=713&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-22-(11)-1"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "797": {
        "name": "ЭГНт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/sonh_po_t/sonh_po.php?action=group&union=0&sid=28702&gr=797&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-23-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "798": {
        "name": "ЭГНт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/sonh_po_t/sonh_po.php?action=group&union=0&sid=28702&gr=798&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-23-(9)-2"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "799": {
        "name": "ЭГНт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/sonh_po_t/sonh_po.php?action=group&union=0&sid=28702&gr=799&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-23-(11)-1"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "823": {
        "name": "ЭГНт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/sonh_po_t/sonh_po.php?action=group&union=0&sid=28702&gr=823&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-24-(9)-1"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "824": {
        "name": "ЭГНт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/sonh_po_t/sonh_po.php?action=group&union=0&sid=28702&gr=824&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-24-(9)-2"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "825": {
        "name": "ЭГНт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/sonh_po_t/sonh_po.php?action=group&union=0&sid=28702&gr=825&year=2025&vr=1",
        "aliases": make_aliases("ЭГНт-24-(11)-1"),
        "department": "СОНХ",
        "specialty": "ЭГНт"
    },
    "642": {
        "name": "МГСт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=642&year=2025&vr=1",
        "aliases": make_aliases("МГСт-21-(9)-1"),
        "department": "ПО",
        "specialty": "МГСт"
    },
    "714": {
        "name": "МГСт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=714&year=2025&vr=1",
        "aliases": make_aliases("МГСт-22-(9)-1"),
        "department": "ПО",
        "specialty": "МГСт"
    },
    "800": {
        "name": "МГСт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=800&year=2025&vr=1",
        "aliases": make_aliases("МГСт-23-(9)-1"),
        "department": "ПО",
        "specialty": "МГСт"
    },
    "826": {
        "name": "МГСт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=826&year=2025&vr=1",
        "aliases": make_aliases("МГСт-24-(9)-1"),
        "department": "ПО",
        "specialty": "МГСт"
    },
    "643": {
        "name": "РСАт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=643&year=2025&vr=1",
        "aliases": make_aliases("РСАт-21-(9)-1"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "644": {
        "name": "РСАт-21-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=644&year=2025&vr=1",
        "aliases": make_aliases("РСАт-21-(9)-2"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "715": {
        "name": "РСАт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=715&year=2025&vr=1",
        "aliases": make_aliases("РСАт-22-(9)-1"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "716": {
        "name": "РСАт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=716&year=2025&vr=1",
        "aliases": make_aliases("РСАт-22-(9)-2"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "717": {
        "name": "РСАт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=717&year=2025&vr=1",
        "aliases": make_aliases("РСАт-22-(11)-1"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "801": {
        "name": "РСАт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=801&year=2025&vr=1",
        "aliases": make_aliases("РСАт-23-(9)-1"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "802": {
        "name": "РСАт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=802&year=2025&vr=1",
        "aliases": make_aliases("РСАт-23-(9)-2"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "803": {
        "name": "РСАт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=803&year=2025&vr=1",
        "aliases": make_aliases("РСАт-23-(11)-1"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "831": {
        "name": "РСАт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=831&year=2025&vr=1",
        "aliases": make_aliases("РСАт-24-(9)-1"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "832": {
        "name": "РСАт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=832&year=2025&vr=1",
        "aliases": make_aliases("РСАт-24-(9)-2"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "833": {
        "name": "РСАт-24-(9)-3",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=833&year=2025&vr=1",
        "aliases": make_aliases("РСАт-24-(9)-3"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "834": {
        "name": "РСАт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=834&year=2025&vr=1",
        "aliases": make_aliases("РСАт-24-(11)-1"),
        "department": "ПО",
        "specialty": "РСАт"
    },
    "646": {
        "name": "СЭЗт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=646&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-21-(9)-1"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "647": {
        "name": "СЭЗт-21-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=647&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-21-(9)-2"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "718": {
        "name": "СЭЗт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=718&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-22-(9)-1"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "719": {
        "name": "СЭЗт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=719&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-22-(9)-2"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "720": {
        "name": "СЭЗт-22-(9)-3",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=720&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-22-(9)-3"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "428": {
        "name": "СЭЗт-22-(9)-4",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=428&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-22-(9)-4"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "721": {
        "name": "СЭЗт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=721&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-22-(11)-1"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "804": {
        "name": "СЭЗт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=804&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-23-(9)-1"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "805": {
        "name": "СЭЗт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=805&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-23-(9)-2"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "806": {
        "name": "СЭЗт-23-(9)-3",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=806&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-23-(9)-3"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "807": {
        "name": "СЭЗт-23-(9)-4",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=807&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-23-(9)-4"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "808": {
        "name": "СЭЗт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=808&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-23-(11)-1"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "827": {
        "name": "СЭЗт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=827&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-24-(9)-1"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "828": {
        "name": "СЭЗт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=828&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-24-(9)-2"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "829": {
        "name": "СЭЗт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=829&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-24-(11)-1"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "830": {
        "name": "СЭЗт-24-(11)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=830&year=2025&vr=1",
        "aliases": make_aliases("СЭЗт-24-(11)-2"),
        "department": "ПО",
        "specialty": "СЭЗт"
    },
    "649": {
        "name": "ЭТЭт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=649&year=2025&vr=1",
        "aliases": make_aliases("ЭТЭт-21-(9)-1"),
        "department": "ПО",
        "specialty": "ЭТЭт"
    },
    "650": {
        "name": "ЭТЭт-21-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=650&year=2025&vr=1",
        "aliases": make_aliases("ЭТЭт-21-(9)-2"),
        "department": "ПО",
        "specialty": "ЭТЭт"
    },
    "722": {
        "name": "ЭТЭт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=722&year=2025&vr=1",
        "aliases": make_aliases("ЭТЭт-22-(9)-1"),
        "department": "ПО",
        "specialty": "ЭТЭт"
    },
    "723": {
        "name": "ЭТЭт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=723&year=2025&vr=1",
        "aliases": make_aliases("ЭТЭт-22-(9)-2"),
        "department": "ПО",
        "specialty": "ЭТЭт"
    },
    "809": {
        "name": "ЭТЭт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=809&year=2025&vr=1",
        "aliases": make_aliases("ЭТЭт-23-(9)-1"),
        "department": "ПО",
        "specialty": "ЭТЭт"
    },
    "810": {
        "name": "ЭТЭт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=810&year=2025&vr=1",
        "aliases": make_aliases("ЭТЭт-23-(9)-2"),
        "department": "ПО",
        "specialty": "ЭТЭт"
    },
    "835": {
        "name": "ЭТЭт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=835&year=2025&vr=1",
        "aliases": make_aliases("ЭТЭт-24-(9)-1"),
        "department": "ПО",
        "specialty": "ЭТЭт"
    },
    "836": {
        "name": "ЭТЭт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28706&gr=836&year=2025&vr=1",
        "aliases": make_aliases("ЭТЭт-24-(9)-2"),
        "department": "ПО",
        "specialty": "ЭТЭт"
    },
    "851": {
        "name": "СПт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=851&year=2025&vr=1",
        "aliases": make_aliases("СПт-24-(9)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "852": {
        "name": "СПт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=852&year=2025&vr=1",
        "aliases": make_aliases("СПт-24-(9)-2"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "853": {
        "name": "СПт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=853&year=2025&vr=1",
        "aliases": make_aliases("СПт-24-(11)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "794": {
        "name": "СПт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=794&year=2025&vr=1",
        "aliases": make_aliases("СПт-23-(9)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "855": {
        "name": "СПт-23-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=855&year=2025&vr=1",
        "aliases": make_aliases("СПт-23-(9)-2"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "856": {
        "name": "СПт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=856&year=2025&vr=1",
        "aliases": make_aliases("СПт-23-(11)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "857": {
        "name": "СПт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=857&year=2025&vr=1",
        "aliases": make_aliases("СПт-22-(9)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "858": {
        "name": "СПт-22-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=858&year=2025&vr=1",
        "aliases": make_aliases("СПт-22-(9)-2"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "859": {
        "name": "СПт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=859&year=2025&vr=1",
        "aliases": make_aliases("СПт-22-(11)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "860": {
        "name": "СПт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=860&year=2025&vr=1",
        "aliases": make_aliases("СПт-21-(9)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "861": {
        "name": "СПт-21-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28704&gr=861&year=2025&vr=1",
        "aliases": make_aliases("СПт-21-(9)-2"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "637": {
        "name": "СПт-21-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=637&year=2025&vr=1",
        "aliases": make_aliases("СПт-21-(9)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "708": {
        "name": "СПт-22-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=708&year=2025&vr=1",
        "aliases": make_aliases("СПт-22-(9)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "709": {
        "name": "СПт-22-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=709&year=2025&vr=1",
        "aliases": make_aliases("СПт-22-(11)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "794": {
        "name": "СПт-23-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=794&year=2025&vr=1",
        "aliases": make_aliases("СПт-23-(9)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "795": {
        "name": "СПт-23-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=795&year=2025&vr=1",
        "aliases": make_aliases("СПт-23-(11)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "818": {
        "name": "СПт-24-(9)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=818&year=2025&vr=1",
        "aliases": make_aliases("СПт-24-(9)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "819": {
        "name": "СПт-24-(9)-2",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=819&year=2025&vr=1",
        "aliases": make_aliases("СПт-24-(9)-2"),
        "department": "СОНХ",
        "specialty": "СПт"
    },
    "820": {
        "name": "СПт-24-(11)-1",
        "url": "https://coworking.tyuiu.ru/shs/all_t/sh.php?action=group&union=0&sid=28703&gr=820&year=2025&vr=1",
        "aliases": make_aliases("СПт-24-(11)-1"),
        "department": "СОНХ",
        "specialty": "СПт"
    }
}

def get_group_by_name(name: str):
    for group_id, group_data in GROUPS_FULL.items():
        if name == group_data["name"]:
            return group_data["name"], group_data
    for group_id, group_data in GROUPS_FULL.items():
        if name in group_data.get("aliases", []):
            return group_data["name"], group_data
    return None, None
    