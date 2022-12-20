from datetime import datetime, timedelta
from enum import Enum
from pyttsx3.engine import Engine

from src.config import ConfigReader


def greet(engine: Engine, config: ConfigReader, delta_time: timedelta):
    day_time = get_day_time()
    text = config.__dict__[day_time._name_].text
    
    if delta_time != timedelta.min:
        total_seconds = delta_time.total_seconds()
        days = total_seconds // 86400
        hours = (total_seconds - days * 86400) // 3600

        text += "\nYou were gone for "
        if days != 0:
            text += f"{int(days)} day{'s' if days > 1 else ''}"
        if hours != 0:
            text += f"{' and' if days != 0 else ''} {int(hours)} hour{'s' if hours > 1 else ''}"

    engine.say(text)
    engine.runAndWait()

def get_day_time():
    now_hour = datetime.now().hour
    if now_hour < 4:
        return DayTime.night
    elif now_hour < 11:
        return DayTime.morning
    elif now_hour < 16:
        return DayTime.monday
    else:
        return DayTime.evening


class DayTime(Enum):
    morning = 1
    monday = 2
    evening = 3
    night = 4

