import pyttsx3
import datetime
from src.config import ConfigReader, CONFIG_PATH
from src.interface import initial_setup


if __name__ == "__main__":
    engine = pyttsx3.init()
    now = datetime.datetime.now()
    config = ConfigReader(CONFIG_PATH, engine)

    if config.is_primary_start:
        initial_setup(engine, config)
        config.is_primary_start = False
        config.save()
    else:
        engine.setProperty("voice", config.voice)
        engine.setProperty("volume", str(config.volume))
        engine.setProperty("rate", str(config.rate))
