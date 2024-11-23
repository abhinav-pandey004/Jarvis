import os
import google.generativeai as genai
api_key = os.environ.get('GOOGLE_API_KEY')

genai.configure(api_key=api_key)
def ai_model(command):
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 2000,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
    ]
    )
    response = chat_session.send_message(command)
    return(response.text.replace("**"," ").replace("*",""))

import webbrowser

def open_url(url):

    webbrowser.open(url, new=2)
search_query = "python programming"
url = f"https://www.google.com/search?q={search_query}"