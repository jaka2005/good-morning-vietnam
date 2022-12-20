import pyttsx3
from pathlib import Path
from datetime import datetime, timedelta

from src.config import ConfigReader, CONFIG_PATH
from src.greeting import greet
from src.interface import initial_setup


def main():
    path_to_config = Path(__file__).parent.joinpath(CONFIG_PATH).resolve()

    engine = pyttsx3.init()
    config = ConfigReader(path_to_config, engine)

    if config.is_primary_start:
        initial_setup(engine, config)
        config.is_primary_start = False
    else:
        engine.setProperty("voice", config.voice)
        engine.setProperty("volume", config.volume)
        engine.setProperty("rate", config.rate)

    now = datetime.now()
    if config.last_time == datetime.min:
        delta_time = timedelta.min
    else:
        delta_time = now - config.last_time

    if delta_time == timedelta.min or delta_time > timedelta(hours=4):
        greet(engine, config, delta_time)

        config.last_time = now
    
    config.save()


if __name__ == "__main__":
    main()