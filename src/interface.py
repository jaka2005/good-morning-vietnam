from typing import Iterable
from pyttsx3.engine import Engine


def test_listen(engine: Engine):
    en_test_text = "Good morning mister James"
    ru_test_text = "Доброе утро, Иван"

    print("en: " + en_test_text)
    engine.say(en_test_text)
    engine.runAndWait()

    print("ru: " + ru_test_text)
    engine.say(ru_test_text)
    engine.runAndWait()

def ask(text: str, answers: Iterable[str] = ("n", "y"), show_options=True) -> str:
    answer = None

    while answer not in answers:
        if show_options:
            print(text, answers, end=" ")
        else:
            print(text, end=" ")
        
        answer = input()

    return answer

def choose_voice(engine: Engine):
    setup = "n"
    while setup != "y":
        voices = engine.getProperty('voices')
        default_voice = engine.getProperty("voice")

        for i, v in enumerate(voices, 1):
            print(str(i) + " - " + v.name)
            
        ans = ask("Enter the voice number", (i + 1 for i in range(len(voices))))
        engine.setProperty("voice", voices[ans - 1].id)

        print("listen:", voices[int(ans) - 1].name)
        test_listen(engine)

        setup = ask("Setup voice?")
        if setup == "n":
            engine.setProperty("voice", default_voice)

def abjust_volume(engine: Engine):
    setup = "n"

    while setup != "y":
        current_volume = engine.getProperty("volume")
        print(
            f"Current volume: {current_volume}\n"
            "Press any key to listen to the test text."
        ); input()

        test_listen(engine)
        
        setup = ask("Are you satisfied with the volume?")

        if setup == "n":
            volume = int(
                ask("Enter the desired volume. (from 0 to 100)",
                (i for i in range(101)), show_options=False)
            ) / 100

            engine.setProperty("volume", volume)

def setup_rate(engine: Engine):
    setup = "n"

    while setup != "y":
        current_rate = engine.getProperty("rate")
        print(
            f"Current volume: {current_rate} words per minute.\n"
            "Press any key to listen to the test text."
        ); input()

        test_listen(engine)
        
        setup = ask("Are you satisfied with the rate?")

        if setup == "n":
            rate = ""
            while type(rate) != "int":
                try:
                    rate = int(
                        ask("Enter the desired rate. (in words per minute)")
                    )
                except ValueError:
                    pass

            engine.setProperty("rate", rate)

def initial_setup(engine: Engine):
    ans = ask(
        "welcome, this is the project \"good morning, vietnam\""
        "it is created for those who are lonely, he can welcome you.\n"
        "do you want to perform the initial setup?"
    )
    
    if ans == "n":
        return
        
    elif ans == "y":
        print("let's choose a voice:")
        choose_voice(engine)
        print("now let's adjust the volume:")
        abjust_volume(engine)
        print("now let's set up the rate:")
        setup_rate(engine)
        