from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from Core_main import getselenium_data
from time import sleep
from respones_data import remove_word_before


def selenium_config():
    # user_data_dir = getselenium_data("seleniumBrowser_data")
    # options = Options()
    # # options.add_experimental_option("detach", True)

    # options.add_argument(f"--user-data-dir={user_data_dir}")
    # options.add_argument(f"--profile-directory=Profile")

    # driver_manager = ChromeDriverManager()  # *selenium and webdriver config function
    # chrome_service = Service(driver_manager.install())
    # driver = webdriver.Chrome(service=chrome_service, options=options)
    driver = webdriver.Chrome()
    return driver

def search_function(audiotext,speak,ttsoutput):  # *web search Functionality  function

    driver = selenium_config()

    new_word_1=remove_word_before(audiotext,"search")

    websearch = "https://www.google.com/search?q="+new_word_1

    driver.get(websearch)

    web_control_function(driver,speak,ttsoutput)


def website_address_searching(
    web_address, speak,ttsoutput
):  # *website address searcing function

    driver = selenium_config()

    driver.get(web_address)

    web_control_function(driver, speak,ttsoutput)



number_words = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
    "thirteenth",
    "fourteenth",
    "fifteenth",
    "sixteenth",
    "seventeenth",
    "eighteenth",
    "nineteenth",
    "twentieth",
    "twenty-first",
    "twenty-second",
    "twenty-third",
    "twenty-fourth",
    "twenty-fifth",
    "twenty-sixth",
    "twenty-seventh",
    "twenty-eighth",
    "twenty-ninth",
    "thirtieth",
    "thirty-first",
    "thirty-second",
    "thirty-third",
    "thirty-fourth",
    "thirty-fifth",
    "thirty-sixth",
    "thirty-seventh",
    "thirty-eighth",
    "thirty-ninth",
    "fortieth",
    "forty-first",
    "forty-second",
    "forty-third",
    "forty-fourth",
    "forty-fifth",
    "forty-sixth",
    "forty-seventh",
    "forty-eighth",
    "forty-ninth",
    "fiftieth",
    "fifty-first",
    "fifty-second",
    "fifty-third",
    "fifty-fourth",
    "fifty-fifth",
    "fifty-sixth",
    "fifty-seventh",
    "fifty-eighth",
    "fifty-ninth",
    "sixtieth",
    "sixty-first",
    "sixty-second",
    "sixty-third",
    "sixty-fourth",
    "sixty-fifth",
    "sixty-sixth",
    "sixty-seventh",
    "sixty-eighth",
    "sixty-ninth",
    "seventieth",
    "seventy-first",
    "seventy-second",
    "seventy-third",
    "seventy-fourth",
    "seventy-fifth",
    "seventy-sixth",
    "seventy-seventh",
    "seventy-eighth",
    "seventy-ninth",
    "eightieth",
    "eighty-first",
    "eighty-second",
    "eighty-third",
    "eighty-fourth",
    "eighty-fifth",
    "eighty-sixth",
    "eighty-seventh",
    "eighty-eighth",
    "eighty-ninth",
    "ninetieth",
    "ninety-first",
    "ninety-second",
    "ninety-third",
    "ninety-fourth",
    "ninety-fifth",
    "ninety-sixth",
    "ninety-seventh",
    "ninety-eighth",
    "ninety-ninth",
]


# *website controling function


def web_control_function(driver, speak,ttsoutput):
    result_list = []
    i = 1
    result_list.append([0, number_words[0]])  # *storing tab index and address
    while True:
        
        try:
            try:
                # Attempt an action with the driver
                driver.current_url
            except WebDriverException:
                driver.quit()
                break
            
            web_audio = ttsoutput()
            web_audio = web_audio.lower()

            if "search" in web_audio:  # *searching functionality
                new_word_1=remove_word_before(web_audio,"search")

                element = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
                element.clear()
                element.send_keys(new_word_1)
                element.send_keys(Keys.ENTER)

            if (
                "click" in web_audio
            ):  #! LOOPHOLE same  word 'open'  and use .com like "facebook.com etc"
                  # * opening functionality
               
                new_word_2=remove_word_before(web_audio,"click")
                elements_with_jsname = driver.find_elements(By.CSS_SELECTOR, "[jsname]")
                for element in elements_with_jsname:

                    link = driver.find_element(
                        By.XPATH, f'//a[contains(@href, "{new_word_2}")]'
                    )
                    link.click()
                    break

            if any(
                word in web_audio for word in ["go", "move", "refresh", "scroll"]
            ):  # * moving back or forward functionality
                if "forward" in web_audio:
                    driver.forward()
                elif any(word in web_audio for word in ["back", "backward"]):
                    driver.back()
                elif "refresh" in web_audio:
                    driver.refresh()
                elif "scroll down" in web_audio:
                    scroll_up_pixels = 500
                    driver.execute_script(f"window.scrollBy(0, {scroll_up_pixels});")
                elif "scroll up" in web_audio:
                    scroll_up_pixels = -500
                    driver.execute_script(f"window.scrollBy(0, {scroll_up_pixels});")

            if (
                any(word in web_audio for word in ["tab"]) and "close" in web_audio
            ):  # * closing tab functionality
                if "all" in web_audio:
                    driver.quit()  # *  closing all tab
                    break
                elif "new" in web_audio:
                    if i > 1:
                        last_window_index = result_list[-1]
                        driver.switch_to.window(
                            driver.window_handles[last_window_index]
                        )  # * closing recent opened tab
                        driver.close()
                        result_list.pop()
                        i -= 1
                elif any(word in web_audio for word in number_words):  # *closing the specific tab
                    txt = web_audio.split()

                    for txt in txt:
                        for word in number_words:
                            if txt == word:
                                requested_string = word
                    corresponding_int = None
                    for pair in result_list:
                        if pair[1] == requested_string:
                            corresponding_int = pair[0]
                    if corresponding_int is not None:
                        driver.switch_to.window(driver.window_handles[corresponding_int])
                        driver.close()
                        # Update the result_list to reflect the closed tab
                        result_list = [pair for pair in result_list if pair[0] != corresponding_int]
                        # Decrement the indices of all tabs that were to the right of the closed tab
                        for pair in result_list:
                            if pair[0] > corresponding_int:
                                pair[0] -= 1
                        i -= 1
            if (
                any(word in web_audio for word in ["tab"]) and any(word in web_audio for word in ["open","switch"])
            ):  # * opening tab functionality

                if "new" in web_audio and "tab" in web_audio:  # * opening new tabs
                    driver.execute_script(
                        "window.open('https://www.google.com', '_blank');"
                    )
                    driver.switch_to.window(driver.window_handles[i])
                    result_list.append([i, number_words[i]])
                    i += 1
                elif any(
                    word in web_audio for word in number_words
                ):  # *swtiching between open the specific tab
                    txt = web_audio.split()

                    for txt in txt:
                        for word in number_words:
                            if txt == word:
                                requested_string = word
                    corresponding_int = None
                    for pair in result_list:
                        if pair[1] == requested_string:
                            corresponding_int = pair[0]

                    if corresponding_int is not None:
                        driver.switch_to.window(
                            driver.window_handles[corresponding_int]
                        )
            if all(
                word in web_audio for word in ["minimise","window"]
            ):  # *Minimizing window  function
                driver.minimize_window()

            if all(
                word in web_audio for word in ["maximize","window"]
            ):  # *maxmixing window  function
                driver.maximize_window()

            if any(word in web_audio for word in ["quit", "exit", "close"]) and all(
                word in web_audio for word in ["web","browser"]
            ):  # *closing  the web browser
                speak("closing webbrowser")
                driver.quit()
                break
            #!extra chrome features
            # if get_keywords("crome_feature.json",web_audio):
            #     keys = get_keywords("crome_feature.json",web_audio)
            #     import pyautogui
            #     pyautogui.hotkey(keys)
            
            
            c = 0
            ###* whatsapp website conditions
            if driver.current_url == "https://web.whatsapp.com/":

                while True:

                    try:
                        if c == 1:
                            web_audio = ttsoutput().lower()
                            
                        if any(word in web_audio for word in ["find"]):

                            try:
                                person = remove_word_before(web_audio,"find")
                                welement = WebDriverWait(driver, 120).until(
                                    EC.presence_of_element_located(
                                        (
                                            By.XPATH,
                                            '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p',
                                        )
                                    )
                                )
                                welement.send_keys(person)
                                welement.send_keys(Keys.ENTER)
                                sleep(0.5)
                                welement.send_keys(Keys.CONTROL + "a")
                                welement.send_keys(Keys.BACKSPACE)
                            except Exception:
                                welement = WebDriverWait(driver, 120).until(
                                    EC.presence_of_element_located(
                                        (
                                            By.XPATH,
                                            '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p',
                                        )
                                    )
                                )
                                welement.send_keys(Keys.CONTROL + "a")
                                welement.send_keys(Keys.BACKSPACE)

                        if all(word in web_audio for word in ["send", "message"]):

                            msg_element = driver.find_element(
                                By.XPATH,
                                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p',
                            )
                            msg_element.send_keys(message)
                            msg_element.send_keys(Keys.ENTER)

                        elif all(word in web_audio for word in ["clear", "message"]):
                            msg_element = driver.find_element(
                                By.XPATH,
                                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p',
                            )
                            msg_element.send_keys(Keys.CONTROL + "a")
                            msg_element.send_keys(Keys.BACKSPACE)
                            
                        elif any(word in web_audio for word in ["type message"]):
                            message = remove_word_before(web_audio,"message")
                            msg_element = driver.find_element(
                                By.XPATH,
                                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p',
                            )
                            msg_element.send_keys(message)
                            message = ""

                        elif all(
                            word in web_audio for word in ["dont", "send", "message"]
                        ) or any(word in web_audio for word in ["no"]):
                            message = ""
                            backelement = driver.find_element(
                                By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/button'
                            )
                            backelement.click

                        else:
                            break

                        c = 1
                    except Exception:
                        pass

        except Exception:
            pass
