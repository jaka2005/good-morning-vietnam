from typing import Iterable
from pyttsx3.engine import Engine


def initial_setup(engine: Engine):
    ans = ask(
        "welcome, this is the project \"good morning, vietnam\""
        "it is created for those who are lonely, he can welcome you.\n"
        "do you want to perform the initial setup?", ("y", "n")
    )
    
    if ans == "n":
        return
    elif ans == "y":
        print("let's choose a voice:")
        choose_voice(engine)


def ask(text, answers: Iterable[str]) -> str:
    answer = None

    while answer not in answers:
        print(text, answers, end=" ")
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
        
        en_test_text = "Good morning mister James"
        ru_test_text = "Доброе утро, Иван"

        print("en: " + en_test_text)
        engine.say(en_test_text)
        engine.runAndWait()

        print("ru: " + ru_test_text)
        engine.say(ru_test_text)
        engine.runAndWait()

        setup = ask("Setup voice?", ("y", "n"))

        if setup == "n":
            engine.setProperty("voice", default_voice)
