import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import json
from colorama import Fore
def chat(assitant_input):
    try:
        with open('geminconfig.json', 'r') as file:
            config = json.load(file)

        #* Accessing the API Key -->
        genai.configure(api_key=config['API']['API_KEY'])

        #* Accessing the Generation Config -->
        generation_config = config['generation_config']

        #* Set Gemini Model Safety Settings -->
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        }

        #* Gemini Model Settings -->
        model = genai.GenerativeModel('gemini-2.0-flash',generation_config=generation_config,safety_settings=safety_settings,system_instruction="Your are Ai Assistant.")
        chat_history = model.start_chat(history=[])
        assitant_response = chat_history.send_message(assitant_input)
        return assitant_response.text
    except Exception as e:
        print(e)
        print(Fore.RED+"Sorry Getting some error. Please try again!!.")