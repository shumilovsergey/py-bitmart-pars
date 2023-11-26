from bs4 import BeautifulSoup
import json
from const import URL
from const import HEADERS
from const import TG_ID
from const import TG_TOKEN
from const import FILE_PATH
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager






def get():
    r = ""
    err = True
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-dev-shm-usage") 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(URL)
        r = driver.page_source
        soup = BeautifulSoup(r, 'html.parser')
        err = False
        print("log: get ok")

    finally:
        driver.quit()
        print("log: get err")
    return soup, err

def tg_alarm(text):
    data = { 
        "chat_id": TG_ID,
        "text": text
    }
    r = requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", data)
    print("log: tg_alarm ok")
    return 

def html_pars(soup):
    nfts_unsort = []
    objects = soup.find_all(class_='nft-card')
    for obj in objects:
        name = obj.find_all(class_='tit')
        name = name[0].text
        price = obj.find_all(class_='usd-price')
        price = price[0].text
        nft = {'name':name, 'price':price}
        nfts_unsort.append(nft)

    print("log: html_pars ok")
    return nfts_unsort

def sort(nfts_unsort):
    nfts_sort = []
    with open(FILE_PATH, 'r') as file:
        last_nfts = json.load(file)

    for last_nft in last_nfts:
        if last_nft not in nfts_unsort:
            last_nfts.remove(last_nft)


    for nft_unsort in nfts_unsort:
        if nft_unsort not in last_nfts:
            nfts_sort.append(nft_unsort)
            last_nfts.append(nft_unsort)
         
    with open(FILE_PATH, 'w') as file:
        json.dump(last_nfts, file, indent=2)

    print("log: sort ok")
    return nfts_sort

def notification(nfts_sort):
    for nft_sort in nfts_sort:
        text = f"🏙 name: {nft_sort['name']}, 💰 price: {nft_sort['price']}"

        data = { 
            "chat_id": TG_ID,
            "text": text
        }
        r = requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", data)
        sleep(1)
        print("log: notification ok")
    return 

def create_json():
    with open(FILE_PATH, 'w') as file:
        json.dump([], file, indent=2)   
    return