from .groups_full_АиЭС import GROUPS_FULL as GROUPS_FULL_AIES
from .groups_full_МПН import GROUPS_FULL as GROUPS_FULL_MPN
from .groups_full_НГО import GROUPS_FULL as GROUPS_FULL_NGO
from .groups_full_СОНХ import GROUPS_FULL as GROUPS_FULL_SONH
from .groups_full_ПО import GROUPS_FULL as GROUPS_FULL_PO

# Объединяем все группы в один словарь
GROUPS_FULL = {}
GROUPS_FULL.update(GROUPS_FULL_AIES)
GROUPS_FULL.update(GROUPS_FULL_MPN)
GROUPS_FULL.update(GROUPS_FULL_NGO)
GROUPS_FULL.update(GROUPS_FULL_SONH)
GROUPS_FULL.update(GROUPS_FULL_PO) 