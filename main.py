
from functions import get
from functions import tg_alarm
from functions import html_pars
from functions import feed_back
from time import sleep


from time import sleep



def main():
    while True:
        r = get()
        if r.status_code != 200:
            tg_alarm(r.status_code)
            break

        else:
            feed_back(html_pars(r))
            sleep(120)

if __name__ == "__main__":
    #   chouse proxi from json
    main()
    