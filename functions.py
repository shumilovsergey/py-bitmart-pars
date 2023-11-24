import requests
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import json

load_dotenv()
TG_ID = os.getenv("TG_ID")
TG_TOKEN = os.getenv("TG_TOKEN")
    



def get(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    r = requests.get(url, headers=headers)
    return r

def tg_alarm(code):
    text = f"Ошибка! Статус код: {code}"
    data = { 
        "chat_id": TG_ID,
        "text": text
    }
    r = requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", data)
    return print(r)

def html_pars(r):

    feed_back = ""
    return feed_back