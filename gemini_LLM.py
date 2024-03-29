import google.generativeai as genai
import os
import dotenv as d
import re
import subprocess
from colorama import Fore
def chat(assitant_input):
    try:
        d.load_dotenv()
        # Set up the model
        generation_config = {
        "temperature": 0.4,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }

        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        ]


        genai.configure(api_key=os.getenv("GEMINI_API"))  ###GEMINI CONFIG
        # text generation model
        model = genai.GenerativeModel(
            "gemini-pro",
            generation_config=generation_config,
            safety_settings=safety_settings,
        )
        chat = model.start_chat(history=[])
        assitant_response = chat.send_message(assitant_input)
        text,code=separate_text_and_code(assitant_response.text)
        return text,code
    except Exception:
        print(Fore.RED+"Sorry Getting some error. Please try again!.")

        

def separate_text_and_code(text):
    pattern = r'```(?:\w+)?\n([\s\S]+?)\n```'
    code_blocks = re.findall(pattern, text)
    placeholder = '__CODE_BLOCK__'
    text_without_code = re.sub(pattern, placeholder, text)
    segments = text_without_code.split(placeholder) 
    segments = [segment.strip() for segment in segments if segment.strip()] 
    return ' '.join(segments), ' '.join(code_blocks)

def Runcode(code):
    file_name="WinOUTPUT"
    errorcheck=0
    with open(file_name, "w") as file:
        for i in code:
            file.write(i)
    try:
        os.system(f"code {file_name}")
    except FileNotFoundError:
        # If VS Code is not found, open the file in Notepad
        os.system(f"notepad {file_name}")
