from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from word2number import w2n
from time import sleep
from respones_data import *
import os
from prompt_toolkit import prompt
from colorama import Fore
def is_convertible(word):
    try:
        w2n.word_to_num(word)
        return True
    except ValueError:
        return False


def convert_to_numbers(input_string):
    for word in input_string.split():
        if is_convertible(word):
            return str(w2n.word_to_num(word))
    return None


def whatsapp_config():
    
    script_directory = os.path.dirname(os.path.abspath(__file__))
    user_data_dir = os.path.join(script_directory,"seleniumBrowser_data")
    options = Options()
    
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument(f"--profile-directory=Profile")
    driver_manager = ChromeDriverManager()  # *selenium and webdriver config function
    chrome_service = Service(driver_manager.install())
    driver = webdriver.Chrome(service=chrome_service, options=options)

    driver.get("https://web.whatsapp.com")
    return driver


def number_of_person(speak,ttsoutput):
    done = True
    while done == True:
        try:
            speak("how many people or group you want to send message")
            num_person = ttsoutput()
            num_person = int(convert_to_numbers(num_person))
            done = False
        except Exception:

            done = True
    return num_person


def send_message(speak, driver, person, message):
    Exception_condi = False
    try:

        welement = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
            )
        )
        welement.send_keys(person)
        welement.send_keys(Keys.ENTER)

        msg_element = driver.find_element(
            By.XPATH,
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p',
        )
        msg_element.send_keys(message)
        msg_element.send_keys(Keys.ENTER)

        sleep(1)
        welement.send_keys(Keys.CONTROL + "a")
        welement.send_keys(Keys.DELETE)

    except Exception:
        Exception_condi = True

    if Exception_condi == True:
        welement = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
            )
        )
        welement.send_keys(Keys.CONTROL + "a")
        welement.send_keys(Keys.BACKSPACE)
        pass


def schedule_and_send_Message(person_list, speak):
    driver = whatsapp_config()
    for person in dict.keys(person_list):
        message = person_list[person]
        send_message(speak, driver, person, message)

    sleep(3)
    driver.close()


def Bulk_message(speak,suggest_message,ttsoutput):

    driver, num_persons = whatsapp_config(), number_of_person(speak)
    Exception_condi = False
    done = False
    while done != True:
        speak("type the message")
        suggestext=suggest_message("write short message on topic")
        message = prompt(f"Enter the message: ",default=suggestext)
        print(Fore.CYAN+"message saved")

        speak("should i confirm the message")
        confirm_message = ttsoutput()
        confirm_message = confirm_message.lower()

        if all(word in confirm_message for word in ["confirm", "message"]) or any(
            word in confirm_message for word in yes_words
        ):
            done = True
        elif all(word in confirm_message for word in ["clear", "message"]) or any(
            word in confirm_message for word in no_words
        ):
            message = ""

    recivers_names = []
    speak("type the reciver names")
    for num_person in range(num_persons):
        recivers_name = input(Fore.GREEN+f"person {num_person+1}:\t")
        recivers_names.append(recivers_name)

    for person in recivers_names:
        try:

            welement = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
                )
            )
            welement.send_keys(person)
            welement.send_keys(Keys.ENTER)

            msg_element = driver.find_element(
                By.XPATH,
                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p',
            )
            msg_element.send_keys(message)
            msg_element.send_keys(Keys.ENTER)

            sleep(1)
            welement.send_keys(Keys.CONTROL + "a")
            welement.send_keys(Keys.DELETE)

        except Exception:
            Exception_condi = True

        if Exception_condi == True:
            print(Fore.RED+f"{person} not found")
            welement = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
                )
            )
            welement.send_keys(Keys.CONTROL + "a")
            welement.send_keys(Keys.BACKSPACE)

    sleep(3)
    driver.close()
