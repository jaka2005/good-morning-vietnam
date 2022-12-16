import pyttsx3
import datetime


if __name__ == "__main__":
    engine = pyttsx3.init()
    now = datetime.datetime.now()

    if 4 <= now.hour <= 11:
        engine.setProperty("rate", 175)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say("good morning mister Jaka")
        engine.runAndWait()




# engine.say("доброе утро, Вьетнам")
# engine.runAndWait()

# rate
# rate = engine.getProperty("rate")
# print(rate)


# engine.say("доброе утро, Хозяин")
# engine.runAndWait()

# voice
# voices = engine.getProperty('voices')
# for i, v in enumerate(voices, 1):
#     print(str(i) + " - " + v.name + " - " + v.id)
#     engine.setProperty('voice', v.id) # second voice (female english) is very cool
#     engine.say("good morning, mister jaka")
#     engine.runAndWait()


# print(engine.getProperty("voice"))

# # volume
# volume = engine.getProperty('volume')
# print(volume)
