"""
bells.py — расписание звонков для пар и перемен
"""

# Время начала первой пары
FIRST_PAIR_START = "8:00"

# Длительность пары в минутах
PAIR_DURATION = 95

# Длительность пятиминутки в минутах
FIVE_MIN_BREAK = 5

# Длительность обычной перемены в минутах
REGULAR_BREAK = 10

# Длительность большой перемены в минутах
LONG_BREAK = 40

# Количество пар
TOTAL_PAIRS = 7

def get_bells_schedule():
    """
    Возвращает расписание звонков в формате:
    [
        {
            "pair": 1,
            "start": "8:00",
            "end": "9:35",
            "break": "9:35-9:45",
            "five_min": "8:45-8:50"
        },
        ...
    ]
    """
    from datetime import datetime, timedelta
    
    schedule = []
    current_time = datetime.strptime(FIRST_PAIR_START, "%H:%M")
    
    for pair in range(1, TOTAL_PAIRS + 1):
        # Начало пары
        pair_start = current_time.strftime("%H:%M")
        
        # Время пятиминутки (через 45 минут после начала пары)
        five_min_start = (current_time + timedelta(minutes=45)).strftime("%H:%M")
        five_min_end = (current_time + timedelta(minutes=50)).strftime("%H:%M")
        
        # Конец пары (начало + 95 минут)
        current_time += timedelta(minutes=PAIR_DURATION)
        pair_end = current_time.strftime("%H:%M")
        
        # Определяем длительность перемены
        if pair == 3:  # После третьей пары большая перемена
            break_duration = LONG_BREAK
        elif pair == 7:  # После седьмой пары нет перемены
            break_duration = 0
        else:
            break_duration = REGULAR_BREAK
        
        # Начало перемены
        break_start = current_time.strftime("%H:%M")
        
        # Конец перемены
        current_time += timedelta(minutes=break_duration)
        break_end = current_time.strftime("%H:%M")
        
        schedule.append({
            "pair": pair,
            "start": pair_start,
            "end": pair_end,
            "break": f"{break_start}-{break_end}" if break_duration > 0 else "нет",
            "five_min": f"{five_min_start}-{five_min_end}"
        })
    
    return schedule

def format_bells_message():
    """
    Форматирует расписание звонков в читаемый текст.
    """
    schedule = get_bells_schedule()
    message = "🔔 Расписание звонков:\n\n"
    
    for pair in schedule:
        message += f"Пара {pair['pair']}:\n"
        message += f"⏰ {pair['start']} - {pair['end']}\n"
        message += f"⏱ Пятиминутка: {pair['five_min']}\n"
        if pair['break'] != "нет":
            message += f"☕ Перемена: {pair['break']}\n"
        message += "\n"
    
    return message

def get_current_pair_info():
    """
    Возвращает информацию о текущей паре и оставшемся времени.
    Возвращает словарь:
    {
        "current_pair": номер текущей пары (1-7) или 0 если сейчас перемена,
        "is_break": True если сейчас перемена,
        "time_left": оставшееся время в минутах,
        "next_event": "пятиминутка" или "конец пары" или "начало пары"
    }
    """
    from datetime import datetime, timedelta
    
    now = datetime.now()
    current_time = now.time()
    schedule = get_bells_schedule()
    
    # Преобразуем время в datetime для удобства сравнения
    current_datetime = datetime.combine(datetime.today(), current_time)
    
    for i, pair in enumerate(schedule, 1):
        start_time = datetime.strptime(pair["start"], "%H:%M").time()
        end_time = datetime.strptime(pair["end"], "%H:%M").time()
        
        # Если сейчас время пары
        if start_time <= current_time < end_time:
            time_to_end = datetime.combine(datetime.today(), end_time) - current_datetime
            minutes_left = int(time_to_end.total_seconds() / 60)
            
            # Если до конца пары больше 5 минут
            if minutes_left > 5:
                return {
                    "current_pair": i,
                    "is_break": False,
                    "time_left": minutes_left - 5,
                    "next_event": "пятиминутка"
                }
            # Если до конца пары 5 минут или меньше
            else:
                return {
                    "current_pair": i,
                    "is_break": False,
                    "time_left": minutes_left,
                    "next_event": "конец пары"
                }
        
        # Если сейчас перемена (и она есть)
        if pair["break"] != "нет":
            break_start = datetime.strptime(pair["break"].split("-")[0], "%H:%M").time()
            break_end = datetime.strptime(pair["break"].split("-")[1], "%H:%M").time()
            
            if break_start <= current_time < break_end:
                time_to_end = datetime.combine(datetime.today(), break_end) - current_datetime
                minutes_left = int(time_to_end.total_seconds() / 60)
                return {
                    "current_pair": 0,
                    "is_break": True,
                    "time_left": minutes_left,
                    "next_event": "начало пары"
                }
    
    # Если сейчас не учебное время
    return {
        "current_pair": 0,
        "is_break": True,
        "time_left": 0,
        "next_event": "начало пары"
    }

def format_time_left_message():
    """
    Форматирует сообщение о текущем времени и оставшемся времени до следующего события.
    """
    info = get_current_pair_info()
    
    if info["current_pair"] == 0:
        if info["time_left"] == 0:
            return "Сейчас не учебное время"
        return f"Сейчас перемена\nДо начала пары осталось {info['time_left']} минут"
    
    if info["is_break"]:
        return f"Сейчас перемена\nДо начала {info['current_pair']} пары осталось {info['time_left']} минут"
    
    # Если идет пара
    message = f"Сейчас идет {info['current_pair']} пара\n"
    
    if info["next_event"] == "пятиминутка":
        message += f"⏰ До пятиминутки осталось {info['time_left']} минут"
    else:
        message += f"⏰ До конца пары осталось {info['time_left']} минут"
    
    return message
