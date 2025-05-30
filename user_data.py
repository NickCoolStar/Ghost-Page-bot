"""
user_data.py — хранение и работа с пользовательскими данными (основная группа)

Использование:
    from user_data import set_user_group, get_user_group

set_user_group(user_id, group_id) — сохранить основную группу пользователя
get_user_group(user_id) — получить сохранённую группу пользователя

Данные хранятся в файле user_data.json (автоматически создаётся и обновляется)
"""

import json
import os
from typing import Dict, Optional
from functools import lru_cache
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Путь к файлу с данными пользователей
USER_DATA_FILE = "user_data.json"

# Кэш для хранения данных пользователей в памяти
_user_groups_cache: Dict[str, str] = {}

def load_user_data() -> Dict[str, str]:
    """
    Загружает данные пользователей из файла user_data.json.
    Использует кэширование для оптимизации повторных чтений.
    
    Returns:
        Dict[str, str]: Словарь user_id -> group_id
    """
    if not _user_groups_cache:
        if os.path.exists(USER_DATA_FILE):
            try:
                with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
                    _user_groups_cache.update(json.load(f))
            except Exception as e:
                logger.error(f"Error loading user data: {e}")
                return {}
    return _user_groups_cache

def save_user_data(data: Dict[str, str]) -> None:
    """
    Сохраняет данные пользователей в файл user_data.json.
    
    Args:
        data: Словарь user_id -> group_id для сохранения
    """
    try:
        with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        # Обновляем кэш
        _user_groups_cache.clear()
        _user_groups_cache.update(data)
    except Exception as e:
        logger.error(f"Error saving user data: {e}")

@lru_cache(maxsize=1000)
def get_user_group(user_id: int) -> Optional[str]:
    """
    Получает сохранённую группу пользователя по user_id.
    Использует кэширование для оптимизации повторных запросов.
    
    Args:
        user_id: ID пользователя в Telegram
        
    Returns:
        Optional[str]: ID группы или None, если группа не найдена
    """
    return load_user_data().get(str(user_id))

def set_user_group(user_id: int, group_name: str) -> None:
    """
    Сохраняет выбранную группу для пользователя.
    
    Args:
        user_id: ID пользователя в Telegram
        group_name: ID группы для сохранения
    """
    data = load_user_data()
    data[str(user_id)] = group_name
    save_user_data(data)
    # Очищаем кэш для этого пользователя
    get_user_group.cache_clear()

# Загружаем данные при старте
load_user_data() 