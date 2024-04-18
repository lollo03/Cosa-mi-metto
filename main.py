import requests
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import date

# Openweather
req_string = f'https://api.openweathermap.org/data/2.5/weather?lat={os.getenv("LAT")}&lon={os.getenv("LON")}&appid={os.getenv("OW_KEY")}&units=metric'

response = requests.get(req_string)

weather = response.json()


del weather["coord"]
del weather["weather"][0]["id"]

today = date.today()
weather["date"] = today.strftime("%B %d, %Y")

print(weather)


# chat gpt falso
headers = {
    'Authorization': f'Bearer {os.getenv("GPT_KEY")}',
    'Content-Type': 'application/json',
}

json_data = {
    'model': 'pai-001-light',
    'max_tokens': 350,
    'messages': [
        {
            'role': 'system',
            'content': 'Sei un assistente che parla solo in inglese, riceverai un testo in formato json con dei dati meteo. Comportati come un meterologo fornendo dei consigli accurati su come vestirsi',
        },
        {
            'role': 'user',
            'content': str(weather),
        },
    ],
}

response = requests.post('https://api.pawan.krd/v1/chat/completions', headers=headers, json=json_data)

gpt_response = response.json()["choices"][0]["message"]["content"]
print(gpt_response)

# api telegram
req_string = f'https://api.telegram.org/bot{os.getenv("TELEGRAM_KEY")}/sendMessage?chat_id={os.getenv("CHAT_ID")}&text={gpt_response}'

response = requests.get(req_string)

print(response.json())