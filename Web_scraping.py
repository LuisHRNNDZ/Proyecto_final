import json
import requests
from bs4 import BeautifulSoup as bs
from deep_translator import GoogleTranslator


def noticias():
    
    document = r"./noticias.txt"
    with open(document, 'w') as f:

        translator = GoogleTranslator(source='auto', target="es")
        apikey="apiKey=532e8814a0c243e9b2823f4a48af16eb"
        url = ("https://newsapi.org/v2/everything?q=computing&sortBy=publishedAt&"
               +apikey)
        
        URL = "https://www.welivesecurity.com/la-es/"
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
                
        r = requests.get(url)
        data = json.loads(r.content)
        articles = data['articles']
        i = 0
        f.write('____________________________________________________________________\n\n')
        f.write('Noticia reciente del api NewsApi\n\n')
        for d in articles:
            if i == 1:
                break
            f.write("Título:"+ translator.translate(d['title'])+"\n")
            f.write("Autor:"+ str(d['author'])+"\n")
            f.write("Fecha de publicación:"+ d['publishedAt']+"\n")
            f.write("Descripción:\n"+ translator.translate(d['description'])+"\n")
            i = i + 1
noticias()
