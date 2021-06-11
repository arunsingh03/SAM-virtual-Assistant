import pyautogui
import pyttsx3 as p
import speech_recognition as sr
import randfacts
import datetime
import pywhatkit

# text to Speech
from YouTube_auto import *
from gettingIpDetails import ip_address_info
from selenium_web import *
from News import *
from Jokes import *
from Weather import *
from gettingRunningTask import *

engine = p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# engine.say("Hello world. I am being born. My name is X.... ")
# engine.say('Hi! .... WHat are you doing?.... I am Listening')
# engine.runAndWait()

def Wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 >= hour < 12:
        return "Morning !"
    elif 12 >= hour < 16:
        return "Afternoon !"
    else:
        return "Evening !"


today_date = datetime.datetime.now()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I Am Listening")
        speak("Listening")
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)
        try:
            print("Recognizing")
            speak("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Say that again Sir")
            return "None"
        return query


# print("Hello Sir! " + "Good " + Wish_me() + "I am your Voice Assistant....X...How Are You?")
# speak("Hello Sir! " + "Good " + Wish_me() + "I am your Voice Assistant....X...How Are You?")


def Hello():
    print("Hello Sir! " + "Good " + Wish_me() + "I am your Voice Assistant....SAM...How Are You?")
    speak("Hello Sir! " + "Good " + Wish_me() + "I am your Voice Assistant....SAM...How Are You?")
    speak("Tell me How can I help You Sir")
    # speak("Tell me How can I help You")


# if "what" and "about" and "you" in listen():
# print("I am also having a great day sir")
# speak("I am also having a great day sir")

# print("what Can I Do for You?")
# speak("what Can I Do for You?")


# with sr.Microphone() as source:
# r.energy_threshold = 10000
# r.adjust_for_ambient_noise(source, 1.2)
# print("Listening...")
# audio = r.listen(source)
# text2 = r.recognize_google(audio)

# text2 = listen()

def Take_query():
    Hello()
    # if "what" and "about" and "you" in listen():
    # print("I am also having a great day sir")
    # speak("I am also having a great day sir")
    # speak("Tell me How can I help You Sir ")
    while True:

        text2 = listen()

        # wikipedia_search
        if "information" in text2:
            speak("You need information related to which topic?")
            # with sr.Microphone() as source:
            # r.energy_threshold = 10000
            # r.adjust_for_ambient_noise(source, 1.2)
            # print("Listening...")
            # audio = r.listen(source)
            # inform = r.recognize_google(audio)
            inform = listen()
            print("Searching {} in wikipedia".format(inform))
            speak("Searching {} in wikipedia".format(inform))
            assist = infow()
            assist.get_info(inform)

        # Youtube_search
        elif "play" and "video" in text2:
            print("Sure Sir! You want  me to play which video?")
            speak("Sure Sir! You want  me to play which video?")
            # with sr.Microphone() as source:
            # r.energy_threshold = 10000
            # r.adjust_for_ambient_noise(source, 1.2)
            # print("Listening...")
            # audio = r.listen(source)
            # YInfo = r.recognize_google(audio)
            info = listen()
            print("playing {} in youtube".format(info))
            speak("playing {} in youtube".format(info))
            assist = music()
            assist.play(info)

        # news_Update
        elif "latest" and "news" in text2:
            print("sure Sir. I will read some latest news for you")
            speak("sure Sir. I will read some latest news for you")
            news_update = news()
            for i in range(len(news_update)):
                print(news_update[i])
                speak(news_update[i])

        # random_facts
        elif "fact" in text2:
            print("Sure Sir, Anything for You")
            speak("Sure Sir, Anything for You")
            fact = randfacts.getFact()
            print(fact)
            speak("Did you know that, " + fact)

        # random_jokes
        elif "joke" in text2:
            print("Sure Sir, get ready for some chuckles! ")
            speak("Sure Sir, get ready for some chuckles! ")
            jk = joke()
            print(jk[0])
            speak(jk[0])
            print(jk[1])
            speak(jk[1])

        elif "temperature" in text2:
            print("Sure Sir!")
            speak("sure Sir!")
            print(
                "Temperature in lucknow today is " + str(temperature()) + " degree Celsius with " + str(description()))
            speak(
                "Temperature in lucknow today is " + str(temperature()) + " degree Celsius with " + str(description()))

        elif "capture" and "screenshot" in text2:
            speak("sure sir! capturing the screenshot of your screen")
            screenshot = pyautogui.screenshot()
            screenshot.save('my_screenshot.png')

        # elif "flip" and "a" and "coin" in text2:
        # speak("Sir sir! Flipping a coin")
        # moves = ["head", "tails"]
        # coin_move = random.moves
        # print(" It's " + coin_move)
        # speak(" It's " + coin_move)

        elif "date" in text2:
            speak("Sure Sir!")
            print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime(
                "%B") + " and It's Currently is " + (
                      today_date.strftime("%I")) + ":" + (today_date.strftime("%M")) + " " + (
                      today_date.strftime("%p")))
            speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime(
                "%B") + " and It's Currently is " + (
                      today_date.strftime("%I")) + " : " + (today_date.strftime("%M")) + " " + (
                      today_date.strftime("%p")))

        elif "message" in text2:
            print("Sure Sir!")
            speak("Sure Sir!")
            speak("please state the number to which you want to send message!")
            phone_no = "+91" + listen()
            speak("Got it Sir")
            speak("Sir what message you want me to send !")
            message = listen()
            speak("Got it Sir")
            speak("Sending Msg Now")
            pywhatkit.sendwhatmsg(phone_no, message, 17, 31)
            print("Sent Successfully")
            speak("Message has been sent")

        elif "task list" in text2 or "task" in text2:
            print('Sure Sir! Showing All Running Tasks!')
            speak('Sure Sir! Showing All Running Tasks!')
            system_info()

        elif "my ip" in text2:
            print("Sure Sir! showing IP Details")
            speak("Sure Sir! showing IP Details")
            ip_address_info()

        elif "bye" in text2:
            print("Bye Bye Sir For Now... I am just one Call Away")
            speak("Bye Bye Sir For Now... I am just one Call Away")
            exit()
        else:
            speak("please Sir Be gentle to Me ")


if __name__ == '__main__':
    # main method for executing
    # the functions
    Take_query()
