
from functions import get
from functions import tg_alarm
from functions import html_pars
from functions import feed_back
from time import sleep


from time import sleep



def main():
    while True:
        url = "https://www.bitmart.com/nft/en-US/collectible?collectibleId=203"
        r = get(url)

        if r.status_code != 200:
            tg_alarm(r.status_code)
            print("!=200")
            break
        else:
            feed_back(html_pars(r))
            
            print("200")
            sleep(120)

if __name__ == "__main__":
    #   chouse proxi from json
    main()
    