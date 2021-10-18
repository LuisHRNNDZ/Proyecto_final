import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.welivesecurity.com/la-es/"

def noticias():
    document = r"./noticias.txt"
    with open(document, 'w') as f:

        page = requests.get(URL)
        soup = bs(page.content, "html.parser") 
        temas = soup.find_all('div', {"class": "text-wrapper col-sm-9 col-xs-8 no-padding"})
        f.write('Las 3 noticias más recientes sobre seguridad informática: \n')
        for i in range(0,3):
            f.write('____________________________________________________________________')
            if i == 0:
                f.write(temas[i].text)
        
            if i == 1:
                f.write(temas[i].text)
        
            if i == 2:
                f.write(temas[i].text)
noticias()
