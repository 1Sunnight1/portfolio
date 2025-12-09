
import requests

# подставьте свои значения
TOKEN = ""  # Ваш токен
CHAT_ID = ""  # Ваш chat_id 

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.get(url, params=params)
    print(response.json())  # Для отладки

# Чтение файла .txt
filename = "message.txt"  # Имя вашего файла
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

send_to_telegram(content)
