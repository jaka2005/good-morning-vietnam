import datetime
from enum import Enum


def greet():
    day_time = get_day_time()
    text = "good " + day_time._name_ + " mister jaka"


def morning_greet():
    ...

def monday_greet():
    ...

def evening_greet():
    ...

def night_greet():
    ...

def get_day_time():
    now_hour = datetime.datetime.now().hour
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

