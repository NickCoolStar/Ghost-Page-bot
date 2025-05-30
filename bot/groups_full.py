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
    }
}

def get_group_by_name(name: str):
    """Find a group by its name or any of its aliases."""
    for group_id, group_data in GROUPS_FULL.items():
        if name in group_data["aliases"]:
            return group_data["name"], group_data
    return None, None 