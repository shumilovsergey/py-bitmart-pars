import requests
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import json

load_dotenv()
TG_ID = os.getenv("TG_ID")
TG_TOKEN = os.getenv("TG_TOKEN")
    



def get():
    url = "https://www.bitmart.com/nft/en-US/collectible?collectibleId=203"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }

    
    r = requests.get(url, headers=headers)
    print(r.content)
    return r

def tg_alarm(code):
    text = f"Ошибка! Статус код: {code}"
    data = { 
        "chat_id": TG_ID,
        "text": text
    }
    r = requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", data)
    return 

def html_pars(r):
    objects = []
    soup = BeautifulSoup(r.text, 'html.parser')
    objects = soup.find_all(class_='nft-card')
    return objects

def feed_back(objects):
    print(objects)
    return