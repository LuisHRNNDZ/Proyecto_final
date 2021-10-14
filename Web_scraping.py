import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.welivesecurity.com/la-es/"

page = requests.get(URL)
soup = bs(page.content, "html.parser") 
temas = soup.find_all('div', {"class": "text-wrapper col-sm-9 col-xs-8 no-padding"})
print ('Las 3 noticias más recientes sobre seguridad informática:')
for i in range(0,3):
    print ('_______________________________________________________________')
    if i == 0:
        temas0 = temas[i].text
        print(temas0)
    if i == 1:
        temas1 = temas[i].text
        print(temas1)
    if i == 2:
        temas2 = temas[i].text
        print(temas2)
