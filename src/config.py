import configparser
from typing import Any
from pyttsx3.engine import Engine


CONFIG_PATH = "./config.ini"


class ConfigReader():
    def __init__(self, config_path, engine: Engine):
        section = "DEFAULT"
        config = configparser.ConfigParser()
        config.read(config_path)
        
        self.is_primary_start = config.getboolean(section, "is_primary_start")
        if self.is_primary_start:
            self.last_time = -1
            self.voice = engine.getProperty("voice")
            config.set(section, "voice", self.voice)
            self.rate = engine.getProperty("rate")
            config.set(section, "rate", self.rate)
            self.volume = engine.getProperty("volume")
            config.set(section, "volume", self.volume)
        else:
            self.last_time = config.getint(section, "last_time")
            self.voice = config.get(section, "voice")
            self.rate = config.get(section, "rate")
            self.volume = config.get(section, "volume")

        self.night = DayTimeConfig(config, "NIGHT")
        self.morning = DayTimeConfig(config, "MORNING")
        self.monday = DayTimeConfig(config, "MONDAY")
        self.evening = DayTimeConfig(config, "EVENING")

        self._section = section
        self._config = config

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ("evening", "monday", "morning", "night"):
            raise AttributeError(f"{self.__class__}.{__name} cannot be set.")
        
        attr_type = type(self.__dir__[__name])
        if type(__value) == attr_type:
            self._config.set(self._section, __name, __value)
            self.__dir__[__name] == __value
        else:
            raise TypeError(f"{self.__class__}.{__name} must be of type {attr_type}")

class DayTimeConfig():
    def __init__(self, config: configparser.ConfigParser, section: str):
        self._text = config.get(section, "text")
        self._config = config
        self._section = section

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._config.set(self._section, "text", value)
