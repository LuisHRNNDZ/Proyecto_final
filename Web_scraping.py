# Librerías necesarias para la información de internet
# Instalar 'pip install beautifulsoup4'
import json
import requests
from bs4 import BeautifulSoup as bs
# Librería para traducir idiomas.
from deep_translator import GoogleTranslator


# Función de trabajo
def noticias():
    document = "./noticias.txt"  # Ruta donde guardaremos la información.
    # Abrimos el documento
    with open(document, 'w') as f:
        # Establecemos el idioma fuenta al idioma que se traducirá.
        translator = GoogleTranslator(source='auto', target="es")
        apikey = "apiKey=532e8814a0c243e9b2823f4a48af16eb"  # apikey de API
        # url a investigar en API
        q = "computing"
        sort = "publishedAT"
        url = (
            "https://newsapi.org/v2/everything?q="+q+"&sortBy="+sort+"+&" +
            apikey
        )
        # url a investigar con beautiful
        URL = "https://www.welivesecurity.com/la-es/"
        page = requests.get(URL)  # Hacemos request a la página.
        soup = bs(page.content, "html.parser")  # Parseamos el contenido
        # Buscamos esas ramas en el html parseado.
        rama = "text-wrapper col-sm-9 col-xs-8 no-padding"
        temas = soup.find_all('div', {"class": rama})
        f.write('Las 3 noticias más recientes sobre seguridad informática: \n')
        # Separamos las noticias que escribiremos en el txt
        for i in range(0, 3):
            f.write('________________________________________________________')
            if i == 0:
                f.write(temas[i].text)
            if i == 1:
                f.write(temas[i].text)
            if i == 2:
                f.write(temas[i].text)
        r = requests.get(url)  # Hacemos request a la API
        data = json.loads(r.content)  # Hacemos el contenido un diccionario
        articles = data['articles']  # Nos ubicamos en los articles de la API
        i = 0
        f.write('________________________________________________________\n\n')
        f.write('Noticia reciente del api NewsApi\n\n')
        # Solo agregamos la primera noticia para complementar las primeras.
        for d in articles:
            if i == 1:
                break
            # Extraemos cada parte que nos interesa de la noticia
            f.write("Título:" + translator.translate(d['title']) + "\n")
            f.write("Autor:" + str(d['author']) + "\n")
            f.write("Fecha de publicación:" + d['publishedAt'] + "\n")
            description = translator.translate(d['description'])
            f.write("Descripción:\n" + description + "\n")
            i = i + 1
noticias()
