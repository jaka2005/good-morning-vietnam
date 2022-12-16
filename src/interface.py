from typing import Iterable
from pyttsx3.engine import Engine

from src.config import ConfigReader


def test_listen(engine: Engine):
    en_test_text = "Good morning mister James"
    ru_test_text = "Доброе утро, Иван"

    print("\nen: " + en_test_text)
    engine.say(en_test_text)
    engine.runAndWait()

    print("ru: " + ru_test_text)
    engine.say(ru_test_text)
    engine.runAndWait()
    print()

def ask(text: str, answers: Iterable[str] = ("n", "y"), show_options=True) -> str:
    answer = None

    while answer not in answers:
        if show_options:
            print(text, answers, end=" ")
        else:
            print(text, end=" ")
        
        answer = input()

    return answer

def choose_voice(engine: Engine, config: ConfigReader):
    voices = engine.getProperty('voices')
    
    setup = "n"
    while setup != "y":
        for i, v in enumerate(voices, 1):
            print(str(i) + " - " + v.name)
        
        print()
        ans = int(ask(
            "Enter the voice number",
            tuple(str(i + 1) for i in range(len(voices)))
        ))
        voice = voices[ans - 1]
        engine.setProperty("voice", voice.id)

        print("\nlisten:", voice.name)
        test_listen(engine)

        setup = ask("Setup voice?")
        print()
    
    config.voice = voice.id

def abjust_volume(engine: Engine, config: ConfigReader):
    setup = "n"
    current_volume = engine.getProperty("volume")

    while setup != "y":
        print(
            f"Current volume: {int(current_volume*100)}\n"
            "Press any key to listen to the test text.", end=" "
        ); input()

        test_listen(engine)
        
        setup = ask("Are you satisfied with the volume?")

        if setup == "n":
            current_volume = int(
                ask("Enter the desired volume. (from 0 to 100)",
                tuple(str(i) for i in range(101)), show_options=False)
            ) / 100

            engine.setProperty("volume", current_volume)
            print()

    config.volume = current_volume

    

def setup_rate(engine: Engine, config: ConfigReader):
    setup = "n"
    current_rate = engine.getProperty("rate")

    while setup != "y":
        print(
            f"Current volume: {current_rate} words per minute.\n"
            "Press any key to listen to the test text.", end=""
        ); input()

        test_listen(engine)
        
        setup = ask("Are you satisfied with the rate?")

        if setup == "n":
            rate = ""
            while type(rate) != int:
                try:
                    rate = int(
                        input("Enter the desired rate (in words per minute): ")
                    )
                except ValueError:
                    pass

            engine.setProperty("rate", rate)
            current_rate = rate
        
        print()

    config.rate = current_rate

def initial_setup(engine: Engine, config: ConfigReader):
    ans = ask(
        "welcome, this is the project \"good morning, vietnam\""
        "it is created for those who are lonely, he can welcome you.\n"
        "do you want to perform the initial setup?"
    )
    
    if ans == "n":
        return

    elif ans == "y":
        print("\nlet's choose a voice:")
        choose_voice(engine, config)
        print("\nnow let's adjust the volume:")
        abjust_volume(engine, config)
        print("\nnow let's set up the rate:")
        setup_rate(engine, config)
        