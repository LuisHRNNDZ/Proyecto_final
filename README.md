 # Scripts para mantenerte al día con la seguridad de tu entorno
  
Sitio de scripts fuente: [Consulta.](https://github.com/LuisHRNNDZ/Proyecto_final)  

## Pre-requisitos :briefcase:
```
  pip install deep-translator
  pip install beautifulsoup4
  pip install bs4
  pip install PyPDF2
  pip install python-nmap
  pip install requests
  pip install machine
```
Instalar todos los modulos con:   
```
 pip install -r requeriments.txt
```

## Estructuramiento :nut_and_bolt:  

Hay 6 scripts escritos induvidualmente:  

  1.- Envio de correo = enviocorreos.py  
  2.- Escaneo de puertos = escaner_ports.py  
  3.- Web scraping = Web_scraping.py  
  4.- Extracción de metadatos de pdf = metadata_pdf.py  
  5.- Cifrado de texto = CifradoCesar.py  
  6.- Descifrado de texto = Desifrado.py  

Y un programa principal: **PIA.py**  
***Hay uno adicional, bruteforce, que toma la url que guardemos en un txt junto con un conjunto de contraseñas y las prueba todas para ver cual funciona***
## Ejecución :gear:  
```
usage: PIA.py [-h] [-w] [-c] [-e] [-d] [-s] [-m] [-f]

optional arguments:
  -h, --help          show this help message and exit
  -w, --web           Activar modulo Web scraping
  -c, --enviocorreo   Activar modulo de Envio de Correo
  -e, --cifradocesar  Activar modulo CifradoCesar
  -d, --descifrado    Activar modulo Descifrado
  -s, --escaneo       Activar modulo Escaneo de Red
  -m, --metadata      Activar modulo metadata
  -f, --force         Fuerza la ejecucion de todos los modulos.
```
Función: el escaneo de puertos generará un txt con los puertos abiertos en ese momento; web scraping generará un txt con noticias extraídas al día sobre el seguridad en información, así como de una API; se hará un pdf de los txt generados y se extrairá los metadatos de ese pdf; se cifrará el texto generado por escaner_ports.py y se creará un txt con el texto cifrado, se creará otro txt con el texto descifrado. Al final se envia un correo de forma automática con la información de web scraping y del escaneo de puertos.

## Soporte y contactos: :email:
luis.lopezh@uanl.edu.mx  
romario.limonhrnd@uanl.edu.mx  
adrian.cortezcs@uanl.edu.mx  
carlos.riveray@uanl.edu.mx  
jesus.desantiagolrg@uanl.edu.mx  
