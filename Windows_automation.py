import pyautogui
import time
from respones_data import remove_word_before
import ctypes


def QuickSettings(text):
    
    if any(word in text for word in ["on","off"]):
        pyautogui.hotkey("win")
        pyautogui.typewrite("setting")
        time.sleep(1)
        pyautogui.hotkey("enter")
        time.sleep(3.5)
        if any(word in text for word in ["wifi"]):
            pyautogui.typewrite("wifi")
            time.sleep(1)
            pyautogui.hotkey("enter")            
            time.sleep(1)
            pyautogui.hotkey("tab")
            pyautogui.hotkey("enter")            
            pyautogui.hotkey("tab")
            time.sleep(1)
            pyautogui.hotkey("tab")
            pyautogui.hotkey("ctrl","space")


        elif any(word in text for word in ["bluetooth"]):
            
            pyautogui.typewrite("Bluetooth and other")
            time.sleep(1)
            pyautogui.hotkey("enter")            
            time.sleep(1)
            pyautogui.hotkey("enter")            
            time.sleep(1)
            pyautogui.hotkey("ctrl","space")
            time.sleep(1)


        elif any(word in text for word in ["airplane mode"]):
            pyautogui.typewrite("airplane mode")
            time.sleep(1)
            pyautogui.hotkey("enter")            
            time.sleep(1)
            pyautogui.hotkey("tab")
            pyautogui.hotkey("enter")             
            time.sleep(1)
            pyautogui.hotkey("ctrl","space")

        elif any(word in text for word in ["hotspot"]):
            pyautogui.typewrite("mobile hotspot")
            time.sleep(1)
            pyautogui.hotkey("enter")            
            time.sleep(1)
            pyautogui.hotkey("tab")
            pyautogui.hotkey("enter")            
            time.sleep(5)
            pyautogui.hotkey("ctrl","space")
        pyautogui.hotkey("alt","f4")

def switch_openapp():
    pyautogui.hotkey("alt","tab")

def minimize_appwindow():
        pyautogui.hotkey("win","d")

def System_SRS(text):
    if any(word in text for word in ["shutdown"]):
        pyautogui.hotkey("win","x")
        pyautogui.press("u")
        pyautogui.press("u")

    if any(word in text for word in ["sign out"]):
        pyautogui.hotkey("win","x")
        pyautogui.press("u")
        pyautogui.press("i")

    if any(word in text for word in ["sleep"]):
        pyautogui.hotkey("win","x")
        pyautogui.press("u")
        pyautogui.press("s")

    if any(word in text for word in ["restart"]):
        pyautogui.hotkey("win","x")
        pyautogui.press("u")
        pyautogui.press("r")

    if any(word in text for word in ["lock"]):
        ctypes.windll.user32.LockWorkStation()

def press_buttons(text):
    keys_to_press = []
    for word in text.split():
        if word.startswith('f'):
            keys_to_press.append(f'F{word[1:]}')
        elif word.lower() == 'window':
            keys_to_press.append('win')
        elif word.lower() == 'space':
            keys_to_press.append("space")
        else:
            keys_to_press.append(word)
    pyautogui.hotkey(*keys_to_press)


def MouseKeyboard_basicOp(text,songsearch,taskmanager):
    time.sleep(1)
    if all(word in text for word in ["select","all"]):
        pyautogui.hotkey("ctrl","a")

    if any(word in text for word in ["type"]):
        sentence = remove_word_before(text,"type")
        pyautogui.typewrite(sentence, interval=0.1)
    
    if any(word in text for word in ["play","pause","start","stop"]):
        if any( word in text for word in ["music", "song"]):
            
            open_app_file("open spotify",taskmanager)
            time.sleep(6)

            songname=remove_word_before(songsearch,"music")
            songname=remove_word_before(songsearch,"song")

            pyautogui.hotkey("ctrl","k")
            pyautogui.hotkey("ctrl","a")
            pyautogui.press("delete")
            time.sleep(2)
            pyautogui.typewrite(songname)
            time.sleep(3)
            pyautogui.hotkey("shift","enter")
            time.sleep(1)
        else:
            pyautogui.hotkey("playpause")

    if "increase" in text:
        if any (word in text for word in ["volume","sound"]):
            pyautogui.hotkey("volumeup")
        else:
            pyautogui.hotkey("f6")
    elif "decrease"  in text:
        if any (word in text for word in ["volume","sound"]):
            pyautogui.hotkey("voulmedown")
        else:
            pyautogui.hotkey("f5")
    elif all (word in text for word in ["mute","volume"]):
        pyautogui.press("volumemute")

    if any(word in text for word in ["enter"]):
        pyautogui.hotkey("enter")
    if any(word in text for word in ["save"]):
        if any(word in text for word in ["as"]):
            pyautogui.hotkey("ctrl","shift","s")
        elif any(word in text for word in ["all"]):
            pyautogui.hotkey("ctrl","alt","s")
    if any(word in text for word in ["find"]):
        pyautogui.hotkey("")    
    if any(word in text for word in ["copy"]):
        if any(word in text for word in ["all"]):
            pyautogui.hotkey("ctrl","a")
            pyautogui.hotkey("ctrl","c")
        else :
            pyautogui.hotkey("ctrl","c")
    if any(word in text for word in ["cut"]):
        if any(word in text for word in ["all"]):
            pyautogui.hotkey("ctrl","a")
            pyautogui.hotkey("ctrl","x")
        else :
            pyautogui.hotkey("ctrl","x")
    if any(word in text for word in ["paste"]):
        pyautogui.hotkey("ctrl","v")
    if any(word in text for word in ["undo","redo"]):
        if any(word in text for word in ["undo"]):
            pyautogui.hotkey("ctrl","z")
        else:
            pyautogui.hotkey("ctrl","y")
    
    if any(word in text for word in ["delete"]):
        pyautogui.hotkey("delete")

    if any(word in text for word in ["close"]):
        pyautogui.hotkey("alt","f4")

    if any(word in text for word in ["refresh"]):
        pyautogui.hotkey("f5")

    if any(word in text for word in ["screen"]):
        if any(word in text for word in ["full"]):
            if any(word in text for word in ["boderless"]):
                pyautogui.hotkey("f11")
            else:
             pyautogui.hotkey("win","up")
        
        if any(word in text for word in ["left"]):
            pyautogui.hotkey("win","left")
        if any(word in text for word in ["right"]):
            pyautogui.hotkey("win","right")

def open_app_file(text,taskmanager):
    admin=False
    if any(word in text for word in ["as administrator","in administrator"]):
        text= text.replace("as administrator","")
        text= text.replace("in administrator","")
        admin=True

    if any(word in text for word in ["open"]):
        new_word_1 = remove_word_before(text,"open")
        if any(word in text for word in ["new"]):
            if any(word in text for word in ["tab","file","folder"]):
                pyautogui.hotkey("ctrl","n")
            elif any(word in text for word in ["window"]):
                pyautogui.hotkey("ctrl","shift","n")
        elif any(word in text for word in ["file","folder"]):
            pyautogui.hotkey("ctrl","o")
            new_word_1 = remove_word_before(new_word_1,"file")
            new_word_1 = remove_word_before(new_word_1,"folder")
            time.sleep(1)
            pyautogui.typewrite(new_word_1)
            pyautogui.hotkey("alt","o")
            
        elif new_word_1 == "copilot":
            pyautogui.hotkey("win","c")
        else:
            if new_word_1 not in (taskmanager.stdout).lower():
                pyautogui.press('win')
                time.sleep(1)
                pyautogui.typewrite(new_word_1)
                time.sleep(1)
                if admin is True:
                    pyautogui.hotkey("ctrl","shift","enter")
                else:
                    pyautogui.press("enter")

def camera_op(text,speak):

        if any(word in text for word in ["change element"]):
            pyautogui.hotkey("tab")

        if any(word in text for word in ["up"]):
            pyautogui.hotkey("up")
        elif any(word in text for word in ["down"]):
            pyautogui.hotkey("down")
        if any(word in text for word in ["record","video"]):
            
            time.sleep(5)
            if any(word in text for word in ["stop"]):
                pyautogui.hotkey("enter")
                time.sleep(1)
                pyautogui.hotkey("down")
            elif any(word in text for word in ["pause","resume"]):
                        pyautogui.hotkey("up")
                        time.sleep(0.5)
                        pyautogui.hotkey("enter")
                        time.sleep(0.5)
                        pyautogui.hotkey("down")
            else:
                speak("Recording in 5 seconds ")
                pyautogui.hotkey("up","up")
                time.sleep(5)
                pyautogui.hotkey("enter")
            
        
        if any(word in text for word in ["click","photo","picture"]):
            speak("Capturing Photo in 5 seconds ")
            time.sleep(5)
            pyautogui.hotkey("enter")
        if any(word in text for word in ["close"]):
            pyautogui.hotkey("alt","f4")
