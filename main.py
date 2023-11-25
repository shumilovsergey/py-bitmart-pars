
from functions import get
from functions import tg_alarm
from functions import html_pars
from functions import sort
from functions import notification
from functions import create_json
from time import sleep
from time import sleep



def main():
    while True:
        soup, err = get()

        if err:
            tg_alarm("Алерт! Нас заблочили. Скрипт остановлен")
            break

        else:
            nfts_unsort = html_pars(soup)
            nfts_sort = sort(nfts_unsort)
            notification(nfts_sort)
            sleep(120)

if __name__ == "__main__":
    create_json()
    main()
    