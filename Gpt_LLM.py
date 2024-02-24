import g4f
import re
import subprocess
from Core_main import set_prefix
import pyautogui

prefix =set_prefix()


Gmessage=[{"role": "assistant","content":"Welcome! I'm Mark, your Windows assistant"},
          {"role": "system","content":"I was created by a group of student"},
          {"role": "system","content":"I can help with tasks like web and Windows automation, gathering real-time information such as weather and news, handling WhatsApp messages and email, providing event alerts, and managing tasks."},
          {"role": "system","content":"Always generate full code inside a code block. and mention the programming language used"},]

def ChatModel(usermessage,speak):
    text,code="",""
    Gmessage.append({"role":"user","content":usermessage})
    
    try:
        response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=Gmessage,
        )
        text,code=separate_text_and_code(response)
        Gmessage.append({"role": "assistant","content":response})
    except Exception:
        speak("sorry i am getting some, issues")
    
    return text,code

def install_missing_module_from_error(error_message):
    # Split the error message by newlines to handle multiple errors
    error_lines = error_message.split('\n')

    for line in error_lines:
        print(line+"\n")
        match_module_not_found = re.search(r"ModuleNotFoundError: No module named '(\w+)'", line)
        if match_module_not_found:
            module_name = match_module_not_found.group(1)
            print(f"Attempting to install {module_name}...")
            subprocess.check_call(["pip", "install", module_name])
            print(f"{module_name} has been successfully installed.")
            return


    print("Could not find a missing module in the error message.")

def separate_text_and_code(text):
    pattern = r'```(?:\w+)?\n([\s\S]+?)\n```'
    code_blocks = re.findall(pattern, text)
    placeholder = '__CODE_BLOCK__'
    text_without_code = re.sub(pattern, placeholder, text)
    segments = text_without_code.split(placeholder) 
    segments = [re.sub(r'[\n\r]+', ' ', segment.strip()) for segment in segments if segment.strip()] 
    return segments,code_blocks

def Runcode(code,speak,text):
    file_name="outputcode"
    errorcheck=0
    done=False
    while done is False:
        with open(file_name, "w") as file:
                        for i in code:
                            file.write(i)
        pyautogui.hotkey("ctrl","p")
        pyautogui.typewrite(file_name)
        pyautogui.press("enter")
        
        if any(word in text for word in ["python","py",".py"]):
            try:
                with open(file_name, "w") as file:
                    for i in code:
                        file.write(i)
                subprocess.run(["python", file_name], capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError as e:
                error_message = str(e.stderr) if e.stderr else str(e)
                install_missing_module_from_error(error_message)
                if errorcheck<=2:
                    ChatModel(f"{error_message} getting this error in the code",speak)
                else:
                    print("sorry! i can't fix the error. please maually solve the error")
                    done=True
                errorcheck+=1
        else:
            done=True
            