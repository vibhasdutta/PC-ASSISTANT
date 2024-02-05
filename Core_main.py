from time import sleep
import subprocess

try:  # * Checking wifi status for connection

    print("Trying to Establishing secure connections...")
    sleep(0.5)
    print("checking for Wifi status")
    sleep(0.5)

    result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
    result.decode("utf-8").strip()

    print("Establishing secure connections success...")
    sleep(0.5)
except:
    print("not connected to Wifi")
    sleep(0.5)
    print("Establishing secure connections failed...")
    sleep(0.5)
    print("Initiating system shutdown protocols...")
    sleep(0.5)
    print("Core functions disengaging....")
    exit()


print("Loading data models and libraries...")
sleep(0.5)
try:
    import pyttsx3
    import speech_recognition as sr
    from dotenv import load_dotenv
    from nltk.tokenize import word_tokenize
    from nltk import pos_tag
    import threading
    import schedule
    import datetime
    import time
    from WebDatabase import *
    from whatsapp_automate_feature import *
    from search_function import *
    from todo_function import *
    from respones_data import *
    from calendar_event_feature import (
        get_events_for_current_date,
        events_calendar,
        eventpop_date,
    )
    from weather_feature_and_location import *
    from Gmail_feature import *
except Exception as E:
    print(E+"\n This Error occured while loading Libraries")
    exit()


load_dotenv()

prefix = ("Win").lower()  # *<--------------- command prefixas


# todo:pyttsx3 COnfig

py = pyttsx3.init()
voice = py.getProperty("voices")
py.setProperty("voice", voice[1].id)
# py.setProperty('pitch', 0.1)
py.setProperty("rate", 165)


# * text to speech function


def speak(text):
    py.say(text)
    py.runAndWait()


def time_guess(hour):
    if "01" <= hour < "13":
        return "goood morning"
    elif "13" <= hour < "18":
        return "goood afternoon"
    elif "18" <= hour <= "23":
        return "goood evening"
    else:
        return


def analyze_noun_text(audiotext):
    # Tokenize the audio text
    words = word_tokenize(audiotext)

    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)

    # Get the current date, time, and day
    now = datetime.datetime.now()
    time_ = now.strftime("%H:%M")
    date = now.strftime("%Y-%m-%d")
    day = now.strftime("%A")

    for word, pos in tagged_words:
        if word.lower() in ["time"] and pos.startswith("NN"):
            speak(f"The time is {time_}")
        if word.lower() in ["date"] and pos.startswith("NN"):
            speak(f"Today's date is {date}")
        if word.lower() in ["day"] and pos.startswith("NN"):
            speak(f"Today is {day}")


# * speech to text function


def ttsoutput():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening..")
        recognizer.adjust_for_ambient_noise(mic, 0.2)
        recognizer.pause_threshold = 350

        audio = recognizer.listen(mic, phrase_time_limit=6)
        text = recognizer.recognize_google(audio)
        print(f"usersaid: {text} ")
    return text

    # * Keyword Dictionarys


#! PLEASE ADD KEYWORD IN SMALL CASE

greeting_list = ["hello", "good morning", "good evening", "good afternoon", "hey"]
exit_list = ["exit", "bye", "good bye"]
web_command_list = ["open web browser", "open chrome", "open browser"]
about_command_list = [
    "are you",
    "about you",
    "made you",
    "aim",
    "purpose",
    "you here",
    "your name",
    "feature",
    "thing",
    "functionality",
    "task",
]
gemini_ai_commmand_list = ["question", "help"]
sleep_word_list = ["wait"]
wakeup_word_list = ["wake", "wake up", "are you there"]


print("Booting up language processing modules...")
sleep(0.5)
print("Syncing with the cloud for real-time updates...")
sleep(0.5)
print("Initializing AI core functions...")
sleep(0.5)
print("Preparing for user interaction...")

core_condition =True
def schedule_():
    while core_condition is not False:
        schedule.run_pending()
        time.sleep(5)


def check_for_events():

    events = eventpop_date()
    attended_event = []

    while core_condition is not False:

        for event in events:

            x = datetime.datetime.now()
            start = event["start"].get("dateTime", event["start"].get("date"))
            start_datetime = datetime.datetime.fromisoformat(start)
            eventtime = start_datetime.strftime("%d/%b/%Y %I:%M %p")
            try:
                if event in attended_event:
                    pass
                elif eventtime == x.strftime("%d/%b/%Y %I:%M %p"):
                    print("\n----EVENT NOTIFICATION----\n")

                    print(f"Event Name: {event['summary']}")
                    print(
                        f"Event Link: {event.get('htmlLink', 'No link available')}\n\n"
                    )
                    attended_event = set(event)
            except Exception as e:
                print(e)

            time.sleep(2)

thr = threading.Thread(target=schedule_)
thr2 = threading.Thread(target=check_for_events)
try:
    thr.start()
    thr2.start()
except Exception as E:
    print(E + "Thread error")


#                                        #todo:                   ---------->MAIN PROGRAM<----------
while True:

    current_time = datetime.datetime.now()
    day = current_time.strftime("%A")
    time_ = current_time.strftime("%I " + "%M " + "%p")
    date = current_time.strftime("%d " + "%B " + "%Y")
    hour = current_time.strftime("%H")

    try:
        audiotext = ttsoutput().lower()

        analyze_noun_text(audiotext)

        # * wake and sleep function

        if any(word in audiotext for word in sleep_word_list):
            speak("ok, wake me up if you need help ")
            while True:
                try:
                    sleep_audiotext = ttsoutput().lower()
                    print(sleep_audiotext)
                    sleep_audiotext = sleep_audiotext.lower()
                    if any(word in sleep_audiotext for word in wakeup_word_list) and f"{prefix}" in sleep_audiotext:
                        speak(are_you_thier())
                        break

                    elif (
                        any(word in sleep_audiotext for word in exit_list)
                        and f"{prefix}" in sleep_audiotext
                    ):

                        if "22" <= hour < "00":
                            speak("goodnight have a good sleep")

                        else:
                            speak("Signing off for now! Until your next deployment!")

                            print("Initiating system shutdown protocols...")
                            sleep(0.7)
                            print("Core functions disengaging....")
                            sleep(0.7)
                        core_condition=False
                        exit()
                    else:
                        print("-----")

                except:
                    pass

        # *Greeting functionalty
        if f"{prefix}" in audiotext:
            if any(word in audiotext for word in greeting_list):
                speak(f"{time_guess(hour)}, {greeting_random()}")

            if any(
                word in audiotext
                for word in [
                    "how are you",
                ]
            ):
                speak(howareyou_response())

            elif any(
                word in audiotext
                for word in [
                    "good job",
                    "you are nice",
                    "well done",
                    "nice",
                    "thanks",
                    "well done",
                    "good",
                    "smart",
                ]
            ):
                speak(appericiation_response())
            elif any(
                word in audiotext
                for word in ["i am also fine", "i am good", "i am fine"]
            ):
                speak(i_am_fine_response())

            if any(word in audiotext for word in wakeup_word_list):
                speak(are_you_thier())
            if any(word in audiotext for word in ["thank you"]):
                speak("your welcome!")


          # * EXITING MAIN FUNCTIONALITY

        if any(word in audiotext for word in exit_list) and f"{prefix}" in audiotext:

            if "22" <= hour < "00":
                speak("goodnight have a good sleep")
            else:
                speak("Signing off for now! Until your next deployment!")

            print("Initiating system shutdown protocols...")
            sleep(0.7)
            print("Core functions disengaging....")
            sleep(0.7)
            core_condition=False
            exit()


          # *todays updates and events detail

        if f"{prefix}" in audiotext:
            if (
                any(word in audiotext for word in ["todays", "today"])
                and any(word in audiotext for word in ["event"])
                and any(word in audiotext for word in ["info", "details"])
            ):
                print("\n")
                get_events_for_current_date(True)
            elif any(word in audiotext for word in ["todays", "today"]) and any(
                word in audiotext for word in ["event"]
            ):
                num = get_events_for_current_date(False)
                speak(f"you have {num} events to attend today")

            elif (
                any(word in audiotext for word in ["upcoming", "coming"])
                and any(word in audiotext for word in ["event"])
                and any(word in audiotext for word in ["info", "details"])
            ):
                print("\n")
                events_calendar(True)
            elif any(word in audiotext for word in ["upcoming", "coming"]) and any(
                word in audiotext for word in ["event"]
            ):
                num = events_calendar(False)
                speak(f"you have {num} events")

            elif any(word in audiotext for word in ["update"]):
                num = get_unread_email_count()
                num2 = get_events_for_current_date(False)
                speak(
                    f"today, you have received {num} emails and, {num2} events to attend"
                )

        # *gemini ai model functionality

        if (
            any(word in audiotext for word in gemini_ai_commmand_list)
            and f"{prefix}" in audiotext
        ):

            if any(word in audiotext for word in ["help"]):
                speak("Sure, I'd be happy to help. What's your question")

            elif any(word in audiotext for word in ["question"]):
                speak("I'm at your service What can I do for you")

        # *Whatsapp send message feature
        if all(
            word in audiotext for word in ["whatsapp", "send", "message", prefix]
        ) and any(word in audiotext for word in ["multiple", "bulk"]):
            Bulk_message(speak)

        elif all(word in audiotext for word in ["whatsapp", "message", prefix]) and any(
            word in audiotext for word in ["schedule"]
        ):
            person_list = {}
            message_schedule = {}

            num_person = number_of_person(speak)
            for _ in range(num_person):
                speak("type the person name")
                name = input("Enter a name: ")
                speak("type the message")
                message = input(f"Enter a message for {name}: ")
                speak("sending time for the message")
                while True:
                    sc_time = input(
                        "Enter the time in 24 Hour format '17:02'(or Enter for ): "
                    )

                    if ":" not in sc_time:
                        print("pls enter the time")
                    else:
                        break

                person_list[name] = message
                message_schedule[name] = sc_time

            for t in message_schedule.values():
                schedule.every().day.at(t).do(
                    lambda: schedule_and_send_Message(person_list, speak)
                )

        elif all(word in audiotext for word in ["whatsapp", "send", "message", prefix]):
            person_list = {}
            num_person = number_of_person(speak)
            for _ in range(num_person):
                speak("type the person name")
                name = input("Enter a name: ")
                speak("type the message")
                message = input(f"Enter a message for {name}: ")
                person_list[name] = message
                schedule_and_send_Message(person_list, speak)

        # *sending emails/read and reply  feature

        if f"{prefix}" in audiotext:
            if any(word in audiotext for word in ["schedule"]) and any(
                word in audiotext for word in ["mail"]
            ):

                while True:
                    speak("is thier any attachments")
                    try:
                        confirm_voice = ttsoutput().lower()
                        if any(word in confirm_voice for word in yes_words):
                            attachements = True
                        elif any(word in confirm_voice for word in no_words):
                            attachements = False
                        else:
                            raise Exception
                        
                        speak("please type the email id")
                        email_id = input("Enter the Email Id\n")

                        speak("type the subject of the email")
                        email_subject = input("Enter the Email Subject\n")

                        speak("please type the email message\n")
                        email_message = input("Enter the Email message\n")

                        speak("sending time for the Email")
                        while True:
                            sc_time = input(
                                "Enter the time in 24 Hour format '17:02'(or Enter for ): "
                            )

                            if ":" not in sc_time:
                                print("pls enter the time")
                            else:
                                break

                        schedule.every().day.at(sc_time).do(
                            lambda: send_email(
                                email_message,
                                email_id,
                                email_subject,
                                attachements,
                                speak,
                            )
                        )
                        break
                    except Exception:
                        pass

            elif any(word in audiotext for word in ["send"]) and any(
                word in audiotext for word in ["mail"]
            ):
                while True:
                    speak("is thier any attachments")
                    try:
                        confirm_voice = ttsoutput().lower()

                        confirm_voice = confirm_voice.lower()
                        if any(word in confirm_voice for word in yes_words):
                            attachements = True
                        elif any(word in confirm_voice for word in no_words):
                            attachements = False
                        else:
                            raise Exception
                        
                        speak("please type the email id")
                        email_id = input("Enter the Email Id\n")

                        speak("type the subject of the email")
                        email_subject = input("Enter the Email Subject\n")

                        speak("please type the email message\n")
                        email_message = input("Enter the Email message\n")

                        send_email(
                            email_message, email_id, email_subject, attachements, speak
                        )
                        break
                    except Exception:
                        pass

            elif any(word in audiotext for word in ["read", "info", "details"]) and any(
                word in audiotext for word in ["mail"]
            ):
                if audiotext:
                    mail_read_and_reply(speak, ttsoutput)
                else:
                    num = get_unread_email_count()
                    speak(f"you have {num} unread emails")

            elif all(word in audiotext for word in ["send", "bulk"]) and any(
                word in audiotext for word in ["mail"]
            ):
                send_bulk_email(speak)

            elif any(word in audiotext for word in ["receive"]) and any(
                word in audiotext for word in ["mail"]
            ):
                num = get_unread_email_count()
                if num > 0:
                    speak(f"yes you have received {num} emails")
                else:
                    speak(f"no you haven't received any emails")

        # *weather and temperature feature

        if any(
            word in audiotext
            for word in [
                "weather",
                "wind speed",
                "humidity",
                "uv",
                "visibility",
                "pressure",
            ]
        ):

            if any(word in audiotext for word in ["in"]):
                try:
                    (
                        temp_celsius,
                        temp_fahrenhite,
                        humidity,
                        pressure,
                        visibility,
                        wind_speed,
                        weather,
                        uv,
                        city,
                        cloud,
                        feelslike_f,
                        feelslike_C,
                    ) = ask_for_city(audiotext=audiotext, speak=speak)

                    if "weather" in audiotext:
                        speak(f"the weather in {city} is {weather}")
                    elif "wind speed" in audiotext:
                        speak(
                            f"the wind speed in {city} is {wind_speed} kilometer per hour"
                        )
                    elif "humidity" in audiotext:
                        speak(f"the humidity in {city} is {humidity}")
                    elif "uv" in audiotext:
                        speak(f"the uv in {city} is {uv}")

                    elif "visibility" in audiotext:
                        speak(f"the visibility in {city} in {visibility} kilometer")
                    elif "pressure" in audiotext:
                        speak(f"the pressure in {city} in {pressure}")

                except Exception:
                    speak("city not found")
            else:
                if "weather" in audiotext:
                    speak(f"the weather in {default_city} is {weather}")
                elif "wind speed" in audiotext:
                    speak(
                        f"the wind speed in {default_city} is {wind_speed} kilometer per hour"
                    )
                elif "humidity" in audiotext:
                    speak(f"the humidity in {default_city} is {humidity}")
                elif "uv" in audiotext:
                    speak(f"the uv in {default_city} is {uv}")
                elif "visibility" in audiotext:
                    speak(f"the visibility in {default_city} in {visibility} kilometer")
                elif "pressure" in audiotext:
                    speak(f"the pressure in {default_city} in {pressure}")

        if "temperature" in audiotext:

            if any(word in audiotext for word in ["in"]):
                try:
                    (
                        temp_celsius,
                        temp_fahrenhite,
                        humidity,
                        pressure,
                        visibility,
                        wind_speed,
                        weather,
                        uv,
                        city,
                        cloud,
                        feelslike_f,
                        feelslike_C,
                    ) = ask_for_city(audiotext=audiotext, speak=speak)

                    if all(word in audiotext for word in ["temperature", "fahrenhite"]):

                        speak(
                            f"the temperature in {city} is {temp_fahrenhite:.1f} fahrenhite and feels like{feelslike_f:.1f} fahrenhite"
                        )

                    elif "hot" in audiotext or "cold" in audiotext:
                        if "cold" in audiotext and -10 < temp_celsius < 20:
                            speak("the temprature in cold outside")
                        elif "hot" in audiotext and 30 < temp_celsius < 100:
                            speak("the temprature is hot outside")
                        else:
                            speak("the temprature is warm outside")
                    else:
                        speak(
                            f"the temperature in {default_city} is {temp_celsius:.1f} celsius and feels like{feelslike_C:.1f} celsius"
                        )
                except Exception:
                    speak("city not found")

            else:
                if all(word in audiotext for word in ["temperature", "fahrenhite"]):

                    speak(
                        f"the temperature in {city} is {temp_fahrenhite:.1f} fahrenhite and feels like{feelslike_f:.1f} fahrenhite"
                    )

                elif "hot" in audiotext or "cold" in audiotext:
                    if "cold" in audiotext and -10 < temp_celsius < 20:
                        speak("the temprature in cold outside")
                    elif "hot" in audiotext and 30 < temp_celsius < 100:
                        speak("the temprature is hot outside")
                    else:
                        speak("the temprature is warm outside")
                else:
                    speak(
                        f"the temperature in {default_city} is {temp_celsius:.1f} celsius and feels like{feelslike_C:.1f} celsius"
                    )

        # * WEBSITE  searching FUNCTIONALITY
        if any(word in audiotext for word in ["search"]):
            search_function(audiotext=audiotext, prefix=prefix, speak=speak)

        # * WEB BROWSER  OPEN  FUNCTIONALITY     
        if any(word in audiotext for word in web_command_list):
            
            while True:
                try:
                    speak("what's the website name?")
                    web_audio = ttsoutput().lower()
                    if web_list_search(web_audio) != "none":
                        websit_adress = web_list_search(web_audio)
                        speak(f"opening {web_audio}")
                        website_address_searching(
                            web_address=websit_adress,
                            speak=speak,
                            web_audio=web_audio,
                        )
                        break
                    elif any(
                        word in web_audio for word in ["close", "exit", "dont open"]
                    ):
                        speak("ok!")
                        break
                    elif web_list_search(web_audio) == "none":
                        #  speak(f" {web_audio} not found in database please add or update it for fast search")
                        #  speak("using search engine please wait")
                        search_engine(web_audio=web_audio, speak=speak)
                        break
                    else:
                        speak("website not found")
                except Exception:
                    pass

        # * TODO  FUNCTIONALITY
        if "notes" in audiotext and any(
            word in audiotext for word in ["make", "add", "create"]
        ):

            todo_add_function(speak=speak)
        elif "notes" in audiotext and any(
            word in audiotext for word in ["delete", "remove"]
        ):
            todo_remove_function(speak=speak)
        elif "notes" in audiotext and any(
            word in audiotext for word in ["update", "change"]
        ):
            todo_update_function(speak=speak)
        elif "notes" in audiotext and any(
            word in audiotext for word in ["open", "preview", "show"]
        ):
            todo_view_function(speak=speak)

        # * about functionality

        if (
            any(word in audiotext for word in about_command_list)
            and f"{prefix}" in audiotext
        ):

            if any(word in audiotext for word in ["who", "what"]):

                speak(
                    f"Hey there! I'm {prefix} and i am not just any PC assistant; I'm your digital sidekick, ready to tackle challenges, simplify tasks, and bring some tech magic into your day"
                )

            if any(
                word in audiotext
                for word in ["feature", "thing", "functionality", "task"]
            ) and any(word in audiotext for word in ["you"]):

                speak(
                    "I can do various type of task's like sending emails, whatsapp message, openning websites , checking for events, wheather reports and more!"
                )

            if any(word in audiotext for word in ["creator", "made you"]):

                speak(
                    "I was created by a student who delved into the world of artificial intelligence. His curiosity and dedication led to the development of the technology that powers me"
                )

                while True:
                    speak("do you  want his contact info ")
                    try:

                        info_audiotext = ttsoutput().lower()
                        if any(word in info_audiotext for word in yes_words):
                            speak("heres all the contact info ")
                            print("https://www.linkedin.com/in/vibhas-dutta-366119248/")
                            print(
                                "https://github.com/vibhasdutta\nEmail ID:vibhasdutta11@gmail.com"
                            )
                            speak("anything else i can do for you")
                            break
                        elif any(word in info_audiotext for word in no_words):
                            speak(
                                "thank you, for adding me into your life and how may i help you"
                            )
                            break
                        else:
                            speak(
                                "thank you, for adding me into your life and how may i help you"
                            )
                            break

                    except Exception:
                        pass

            if any(word in audiotext for word in ["you"]) and any(
                word in audiotext for word in ["aim", "purpose"]
            ):
                speak(aim_response(prefix=prefix))

    except sr.UnknownValueError:
          pass
