# Telegram Bot для просмотра расписания ТИУ

Бот для просмотра расписания групп Тюменского индустриального университета через Telegram.

## Возможности

- Выбор отделения, специальности и группы
- Сохранение основной группы пользователя
- Просмотр расписания через скриншоты
- Поддержка альтернативных названий групп (алиасов)
- Автоматическое обновление списка групп

## Установка

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
cd <папка-проекта>
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите браузер для Playwright:
```bash
playwright install chromium
```

4. Создайте файл `secrets.py` с токеном вашего бота:
```python
secret_key = "ваш_токен_бота"
```

## Структура проекта

- `main.py` - основной файл бота
- `parse_groups.py` - скрипт для обновления списка групп
- `groups_full.py` - файл с данными о группах
- `user_data.py` - хранение пользовательских данных
- `secrets.py` - конфиденциальные данные (токены)

## Запуск

1. Обновите список групп:
```bash
python bot/parse_groups.py
```

2. Запустите бота:
```bash
python bot/main.py
```

## Использование

1. Найдите бота в Telegram по его имени
2. Отправьте команду `/start`
3. Следуйте инструкциям бота:
   - Выберите отделение
   - Выберите специальность
   - Выберите группу
   - Просматривайте расписание

## Обновление списка групп

Для обновления списка групп выполните:
```bash
python bot/parse_groups.py
```

Скрипт автоматически:
- Соберёт актуальный список групп
- Сгенерирует алиасы
- Обновит файл `groups_full.py`

## Требования

- Python 3.8+
- python-telegram-bot
- playwright
- Доступ к сайту расписания ТИУ

## Устранение неполадок

1. Если бот не отвечает:
   - Проверьте подключение к интернету
   - Убедитесь, что токен бота верный
   - Проверьте логи на наличие ошибок

2. Если не отображаются скриншоты:
   - Проверьте установку Playwright
   - Убедитесь, что сайт расписания доступен
   - Проверьте права доступа к папке

3. Если не обновляется список групп:
   - Проверьте доступ к сайту расписания
   - Убедитесь, что структура сайта не изменилась
   - Проверьте логи скрипта обновления

## Поддержка

При возникновении проблем:
1. Проверьте раздел "Устранение неполадок"
2. Посмотрите логи бота
3. Создайте issue в репозитории проекта

## Лицензия

MIT License 