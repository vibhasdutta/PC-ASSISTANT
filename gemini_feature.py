import google.generativeai as genai
import os
import dotenv as d


def chat():
    d.load_dotenv()
    generation_config = {
        "temperature": 0.0,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
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

    # assitant_input = ttsoutput()
    while True:

        assitant_response = input("enter")
        assitant_response = chat.send_message(assitant_response)

        print(assitant_response.text)
        break


chat()
