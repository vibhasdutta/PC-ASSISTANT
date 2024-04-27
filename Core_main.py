def getselenium_data(folder_name:str):
    import os
    script_directory = os.path.dirname(os.path.abspath(__file__))
    user_data_dir = os.path.join(script_directory,folder_name)
    return user_data_dir

def set_prefix():  # *=============== command prefixas
    import os
    import dotenv
    dotenv.load_dotenv()
    prefix = os.getenv("PREFIX").lower()
    return prefix

if __name__ == "__main__":
    from colorama import Fore
    from time import sleep
    import subprocess
    import time
    start_time = time.time()

    try:  # *===============  Checking Internet status for connection

        print(Fore.MAGENTA+"Trying to Establishing secure connections...")
        sleep(0.5)
        print(Fore.MAGENTA+"checking for Internet status")
        sleep(0.5)

        result = subprocess.check_output(["ping", "www.google.com"])
        print(Fore.MAGENTA+"Establishing secure connections success...")
        sleep(0.5)
    except:
        print(Fore.MAGENTA+"not connected to Internet")
        sleep(0.5)
        print(Fore.MAGENTA+"Establishing secure connections failed...")
        sleep(0.5)
        print(Fore.MAGENTA+"Initiating system shutdown protocols...")
        sleep(0.5)
        print(Fore.MAGENTA+"Core functions disengaging....")
        exit()

    while True:
        print(Fore.MAGENTA+"Loading data models and libraries...")
        sleep(0.5)
        try:
            import pyttsx3
            import speech_recognition as sr
            
            from dotenv import load_dotenv
            #*nltk libraries
            import nltk
            nltk.download(["punkt","averaged_perceptron_tagger",'words','stopwords'])
            from nltk.tokenize import word_tokenize
            from nltk.corpus import stopwords
            from nltk import pos_tag

            import threading
            import schedule
            import datetime
            from prompt_toolkit import prompt
            import tkinter as tk
            from tkinter import filedialog
            from Windows_automation import *
            from WebDatabase import *
            from whatsapp_automate_feature import *
            from search_function import *
            from Task import *
            from respones_data import *
            from gemini_LLM import *
            from calendar_event_feature import (
                get_events_for_current_date,
                events_calendar,
                eventpop_date,
            )
            from weather_feature_and_location import *
            from Gmail_feature import *
            from city_name_database import findcityname
            
            break
        except Exception as E:
            print(Fore.RED+"\n Error occured while loading Libraries")

    print(Fore.MAGENTA+"Booting up language processing modules...")
    sleep(0.5)
    print(Fore.MAGENTA+"Syncing with the cloud for real-time updates...")
    sleep(0.5)
    print(Fore.MAGENTA+"Initializing AI core functions...")
    sleep(0.5)
    print(Fore.MAGENTA+"Preparing for user interaction...")

    load_dotenv()

    
    # todo:=======pyttsx3 COnfig

    py = pyttsx3.init()
    voice = py.getProperty("voices")
    py.setProperty("voice", voice[1].id)
    # py.setProperty('pitch', 0.1)
    py.setProperty("rate", 165)

    prefix = set_prefix()
    core_condition = True  #!CORE CONDITION!

    # *===============  text to speech function
    def speak(text):
        py.say(text)
        py.runAndWait()
        
    # *===============  speech to text function
    def ttsoutput():
        recognizer = sr.Recognizer()
        with sr.Microphone(sample_rate=16000, chunk_size=512) as mic:
            print(Fore.YELLOW+"Listening..")
            recognizer.non_speaking_duration = 0
            recognizer.pause_threshold = 190  # Adjust this value based on the speed of speech
            recognizer.adjust_for_ambient_noise(mic, duration=0.4)
            audio = recognizer.listen(mic, phrase_time_limit=4) # Reduce the phrase_time_limit
            text = recognizer.recognize_google(audio, language='en-IN', show_all=False)
            print(Fore.CYAN+f"usersaid: {text} ")
        return text

    def suggest_message(typeofmessage: str):
        while True:
            try:
                speak("would you like me to suggest a message")
                suggest_text = ttsoutput().lower()
                if any(word in suggest_text for word in yes_words):
                    speak("can you tell me about the message")
                    suggest_text = ttsoutput().lower()
                    suggest_text = f"{typeofmessage} {suggest_text}"
                    text,code= chat(suggest_text)
                    return text
                else:
                    return ""
                    
            except Exception:
                pass

    def Tokenize_Verb(audiotext):
        # Tokenize the audio text
        words = word_tokenize(audiotext)

        # Perform part-of-speech tagging
        tagged_words = pos_tag(words)

        return tagged_words

    def remove_stopwords(text):
        # Tokenize the text into words
        words = word_tokenize(text)
        
        # Get the English stopwords from NLTK
        stop_words = set(stopwords.words('english'))
        
        # Filter out the stop words
        filtered_words = [word for word in words if word.lower() not in stop_words]
        
        # Join the remaining words back into a single string
        filtered_text = ' '.join(filtered_words)
        
        return filtered_text
    

    def select_file():
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        file_path = ""
        while True:
            speak("is thier any attachments")
            try:
                confirm_voice = ttsoutput().lower()
                if any(word in confirm_voice for word in yes_words):
                    file_path = filedialog.askopenfilename(title="Select File")
                    attachements = "True"
                    return file_path, attachements

                elif any(word in confirm_voice for word in no_words):
                    attachements = "False"
                    return file_path, attachements
                root.destroy()  # Destroy the Tkinter window after file selection

            except Exception:
                pass

    def time_guess(hour):
        if "01" <= hour < "13":
            return "goood morning"
        elif "13" <= hour < "18":
            return "goood afternoon"
        elif "18" <= hour <= "23":
            return "goood evening"
        else:
            return

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
                except Exception:
                    print(Fore.RED+"Error in event checking")

                time.sleep(2)

    Schedule_thread = threading.Thread(target=schedule_)
    checkevents_thread = threading.Thread(target=check_for_events)
    try:
        Schedule_thread.start()
        checkevents_thread.start()
    except Exception as E:
        print(Fore.RED+"Error in starting thread")

    #                                        #todo:                   ---------->MAIN PROGRAM<----------
    while True:
        
        current_time = datetime.datetime.now()
        day = current_time.strftime("%A")
        time_ = current_time.strftime("%I " + "%M " + "%p")
        date = current_time.strftime("%d " + "%B " + "%Y")
        hour = current_time.strftime("%H")
        try:
            audiotext = ttsoutput().lower()
            
            if f"ok {prefix}" not in audiotext and prefix in audiotext:
                audiotext = audiotext.replace(f"{prefix}", "") #due to g4f lib issuses
                try:
                    text,code = chat(audiotext)
                    speak(text)
                    if code:
                        Runcode(code)
                except Exception:
                    speak("Sorry Getting some error. Please try again!.")
                    continue
                # *===============  wake and sleep function
                if any(word in audiotext for word in sleep_word_list):
                    speak("wake me up if you need help ")
                    while True:
                        try:
                            sleep_audiotext = ttsoutput().lower()
                            sleep_audiotext = sleep_audiotext.replace(f"{prefix}", "")
                            if any(
                                word in sleep_audiotext for word in wakeup_word_list
                            ):
                                try:
                                    text,code = chat(sleep_audiotext)
                                    speak(text)
                                    if code:
                                        pass
                                except Exception:
                                    speak("Sorry Getting some error. but i am here!.")
                                break
                            elif any(word in sleep_audiotext for word in exit_list):
                                if "22" <= hour < "00":
                                    speak("goodnight have a good sleep")
                                    core_condition = False
                                    exit()
                                else:
                                    speak(
                                        "Signing off for now! Until your next deployment!"
                                    )
                                    print(Fore.MAGENTA+"Initiating system shutdown protocols...")
                                    sleep(0.7)
                                    print(Fore.MAGENTA+"Core functions disengaging....")
                                    sleep(0.7)
                                    core_condition = False
                                    exit()
                        except:
                            pass

                # *===============  EXITING MAIN FUNCTIONALITY
                if any(word in audiotext for word in exit_list):
                    if "22" <= hour < "00":
                        speak("goodnight have a good sleep")
                    else:
                        speak("Signing off for now! Until your next deployment!")
                    print(Fore.MAGENTA+"Initiating system shutdown protocols...")
                    sleep(0.7)
                    print(Fore.MAGENTA+"Core functions disengaging....")
                    sleep(0.7)
                    core_condition = False
                    exit()

            elif f"ok {prefix}"in audiotext:
                audiotext = audiotext.replace(f"ok {prefix}", "")
                suggestext=""
                temptext=audiotext #! text with stop  word for searching and controlling command 
                tagged_words = Tokenize_Verb(audiotext)
                audiotext=remove_stopwords(audiotext)
                taskmanager=subprocess.run(['tasklist'], capture_output=True, text=True)
                
                if any(word in audiotext for word in ["time", "date", "day", "hour"]):
                    for word, pos in tagged_words:
                        if word.lower() in ["hour"] and pos.startswith("NN"):
                            speak(f"the hour is {hour}")
                        if word.lower() in ["date"] and pos.startswith("NN"):
                            speak(f"today's date is {date}")
                        if word.lower() in ["time"] and pos.startswith("NN"):
                            speak(f"the time is {time_}")
                        if word.lower() in ["day"] and pos.startswith("NN"):
                            speak(f"today is {day}")            


                # *=============== todays updates and events detail

                if (
                    any(word in audiotext for word in ["todays", "today"])
                    and any(word in audiotext for word in ["event"])
                    and any(word in audiotext for word in ["info", "details"])
                ):
                    get_events_for_current_date(True)
                elif any(word in audiotext for word in ["todays", "today"]) and any(
                    word in audiotext for word in ["event"]
                ):
                    num = get_events_for_current_date(False)
                    speak(f"you have {num} event's to attend today")
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
                    speak(f"you have {num} event's")
                elif any(word in audiotext for word in ["update"]):
                    num = get_unread_email_count()
                    num2 = get_events_for_current_date(False)
                    speak(
                        f"today, you have received {num} emails and, {num2} event's to attend"
                    ) 
                        
                # *=============== Whatsapp send message feature
                if all(word in audiotext for word in ["whatsapp",  "message"]) :
                    
                    if any(word in audiotext for word in ["multiple", "bulk"]):
                        Bulk_message(speak,ttsoutput)
                    elif  any(word in audiotext for word in ["schedule"]):
                        person_list = {}
                        message_schedule = {}
                        num_person = number_of_person(speak,ttsoutput)
                        for _ in range(num_person):
                            speak("type the person name")
                            name = input(Fore.GREEN+"Enter a name: ")
                            speak("type the message")
                            suggestext=suggest_message("write short message on topic")
                            message = prompt(f"Enter a message for {name}: ",default=suggestext)
                            speak("sending time for the message")
                            while True:
                                sc_time = input(
                                    Fore.GREEN+"Enter the time in 24 Hour format '17:02'(or Enter for ): "
                                )
                                if ":" not in sc_time:
                                    print(Fore.CYAN+"pls enter the time")
                                else:
                                    break
                            person_list[name] = message
                            message_schedule[name] = sc_time
                        for t in message_schedule.values():
                            schedule.every().day.at(t).do(
                                lambda: schedule_and_send_Message(person_list, speak)
                            )
                    elif  any(word in audiotext for word in ["send"]):
                        person_list = {}
                        num_person = number_of_person(speak,ttsoutput)
                        for _ in range(num_person):
                            speak("type the person name")
                            name = input(Fore.GREEN+"Enter a name: ")
                            speak("type the message")
                            suggestext=suggest_message("write short message on topic")
                            message = prompt(f"Enter a message for {name}: ",default=suggestext)
                            person_list[name] = message
                        schedule_and_send_Message(person_list, speak)
                # *=============== sending emails/read and reply  feature
                if any(word in audiotext for word in ["schedule"]) and any(
                    word in audiotext for word in ["mail"]
                ):
                    file_path, attachements = select_file()
                    speak("please type the email id")
                    email_id = input(Fore.GREEN+"Enter the Email Id\n")
                    speak("type the subject of the email")
                    email_subject = input(Fore.GREEN+"Enter the Email Subject\n")
                    speak("please type the email message\n")
                    suggestext=suggest_message("write email body message on topic")
                    email_message = prompt("Enter the Email message\n",default=suggestext)
                    speak("sending time for the Email")
                    while True:
                        sc_time = input(
                            Fore.GREEN+"Enter the time in 24 Hour format '17:02'(or Enter for ): "
                        )
                        if ":" not in sc_time:
                            print(Fore.CYAN+"pls enter the time")
                        else:
                            break
                    
                    
                    schedule.every().day.at(sc_time).do(
                        lambda: send_email(
                            email_message,
                            email_id,
                            email_subject,
                            attachements,
                            file_path,
                            speak,
                        )
                    )
                    break
                        
                elif any(word in audiotext for word in ["send"]) and any(
                    word in audiotext for word in ["mail"]
                ):

                    file_path, attachements = select_file()
                    speak("please type the email id")
                    email_id = input(Fore.GREEN+"Enter the Email Id\n")
                    speak("type the subject of the email")
                    email_subject = input(Fore.GREEN+"Enter the Email Subject\n")
                    speak("please type the email message\n")
                    suggestext=suggest_message("write email body message on topic")
                    email_message = prompt("Enter the Email message\n",default=suggestext)
                    send_email(email_message,email_id,email_subject,attachements,file_path,speak)
                    break
                        

                elif any(
                    word in audiotext for word in ["read", "info", "details"]
                ) and any(word in audiotext for word in ["mail"]):
                    if audiotext:
                        mail_read_and_reply(speak, ttsoutput)
                    else:
                        num_unread_email = get_unread_email_count()
                        speak(f"you have {num_unread_email} unread emails")
                        
                elif all(word in audiotext for word in ["send", "bulk"]) and any(
                    word in audiotext for word in ["mail"]
                ):
                    file_path, attachements = select_file()
                    send_bulk_email(attachements, file_path, speak,suggest_message)
                    break

                elif any(word in audiotext for word in ["receive"]) and any(
                    word in audiotext for word in ["mail"]
                ):
                    num_unread_email = get_unread_email_count()
                    if  num_unread_email > 0:
                        speak(f"yes you have received {num_unread_email} emails")
                    else:
                        speak(f"no you haven't received any emails")

                # *===============  WEBSITE  searching FUNCTIONALITY
                if any(word in audiotext for word in ["search"]):
                    search_function(audiotext=temptext, speak=speak,ttsoutput=ttsoutput,)
                
                # *===============  WEB BROWSER  OPEN  FUNCTIONALITY
                if "open" in audiotext and any(
                    word in audiotext for word in web_command_list
                ):

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
                                    ttsoutput=ttsoutput,
                                )
                                break
                            elif any(word in web_audio for word in no_words) or any(word in web_audio for word in ["close","exit"]) :
                                speak("ok!")
                                break
                            elif web_list_search(web_audio) == "none":
                                search_function(web_audio,speak,ttsoutput=ttsoutput,)
                                break
                        except Exception:
                            pass
                # *windows automation
                MouseKeyboard_basicOp(audiotext,temptext,taskmanager)

                if "open" in audiotext and not any(
                    word in audiotext for word in web_command_list
                ):
                    open_app_file(audiotext,taskmanager)

                if "type" not in audiotext and "press" in audiotext:
                    press_buttons(temptext)

                camera_op(audiotext, speak)

                for word, pos in tagged_words:
                    if word.lower() in ["off", "on"] and pos.startswith("IN"):
                        QuickSettings(temptext)

                if "pc" in audiotext:
                    System_SRS(audiotext)

                if (
                    any(word in audiotext for word in ["minimise", "maximize", "hide"])
                    and "window" in audiotext
                ):
                    minimize_appwindow()

                if any (word in audiotext for word in ["switch", "change", "next","goto"]):
                    
                        switch_openapp()

                # *=============== weather and temperature feature

                if any(
                    word in audiotext
                    for word in [
                        "weather",
                        "wind speed",
                        "humidity",
                        "uv",
                        "visibility",
                        "pressure",
                        "temperature",
                    ]
                ):
                    cityname = findcityname(audiotext)
                    if cityname :

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
                            ) = ask_for_city(cityname)
                    else:
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
                            ) = ask_for_city(cityname)

                    if "weather" in audiotext:
                        speak(f"the weather in {city} is {weather}")
                    if "wind speed" in audiotext:
                        speak(
                            f"the wind speed in {city} is {wind_speed} kilometer per hour"
                        )
                    if "humidity" in audiotext:
                        speak(f"the humidity in {city} is {humidity}")
                    if "uv" in audiotext:
                        speak(f"the uv in {city} is {uv}")
                    if "visibility" in audiotext:
                        speak(
                            f"the visibility in {city} in {visibility} kilometer"
                        )
                    if "pressure" in audiotext:
                        speak(f"the pressure in {city} in {pressure}")
                    
                    if any(
                        word in audiotext
                        for word in ["temperature"]
                    ):
                        if any(
                            word in audiotext
                            for word in ["fahrenhite"]
                        ):
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
                                f"the temperature in {city} is {temp_celsius:.1f} celsius and feels like{feelslike_C:.1f} celsius"
                            )



                # *===============  Task  FUNCTIONALITY

                if any(word in audiotext for word in ["add","delete","show"])and "task" in audiotext:
                    if "add" in audiotext:
                        create_task(speak,ttsoutput)
                    elif "delete" in audiotext:
                        delete_task(speak,ttsoutput)
                    elif "show" in audiotext:
                        show_tasks(speak,ttsoutput)                 
        except KeyboardInterrupt:
            pass
        except sr.UnknownValueError:
            pass
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")              
        #!IF you want to see the memory usage of the program->
        import os
        import psutil
        def print_memory_usage():
            process = psutil.Process(os.getpid())
            memory_info = process.memory_info()
            print(f"Memory used by this program: {memory_info.rss / 1024 / 1024} MB")
        print_memory_usage() 