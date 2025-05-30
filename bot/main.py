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

from bot.secrets import secret_key
from bot.groups_full import GROUPS_FULL, get_group_by_name
from bot.user_data import set_user_group, get_user_group
from bot.bells import format_bells_message, format_time_left_message

# ... rest of the file remains unchanged ... 