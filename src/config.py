import configparser
from typing import Any
from pyttsx3.engine import Engine


CONFIG_PATH = "./config.ini"


class ConfigReader():
    def __init__(self, config_path, engine: Engine):
        section = "DEFAULT"
        config = configparser.ConfigParser()
        config.read(config_path)
        
        self.__dict__["is_primary_start"] = config.getboolean(section, "is_primary_start")
        if self.is_primary_start:
            self.__dict__["last_time"] = -1
            self.__dict__["voice"] = engine.getProperty("voice")
            config.set(section, "voice", self.voice)
            self.__dict__["rate"] = engine.getProperty("rate")
            config.set(section, "rate", self.rate)
            self.__dict__["volume"] = engine.getProperty("volume")
            config.set(section, "volume", self.volume)
        else:
            self.__dict__["last_time"] = config.getint(section, "last_time")
            self.__dict__["voice"] = config.get(section, "voice")
            self.__dict__["rate"] = config.get(section, "rate")
            self.__dict__["volume"] = config.get(section, "volume")

        self.__dict__["night"] = DayTimeConfig(config, "NIGHT")
        self.__dict__["morning"] = DayTimeConfig(config, "MORNING")
        self.__dict__["monday"] = DayTimeConfig(config, "MONDAY")
        self.__dict__["evening"] = DayTimeConfig(config, "EVENING")

        self.__dict__["_section"] = section
        self.__dict__["_config "]= config

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ("evening", "monday", "morning", "night", "_section", "_config"):
            raise AttributeError(f"{self.__class__}.{__name} cannot be set.")
        
        attr_type = type(self.__dict__[__name])
        if type(__value) == attr_type:
            self._config.set(self._section, __name, __value)
            self.__dict__[__name] == __value
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
