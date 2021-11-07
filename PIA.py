import Web_scraping as webscrap
import enviocorreos as correo
import escaner_ports as escan
import CifradoCesar as cifrado
import Descifrado as desci
import metadata_pdf as meta
import bruteforce as brutef
import json
import argparse
import sys
import logging
logging.basicConfig(filename='logging',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'
my_parser.add_argument(
    '-w', '--web', help="Activar modulo Web scraping", action='store_true')
my_parser.add_argument(
    '-c', '--enviocorreo',
    help="Activar modulo de Envio de Correo ",
    action='store_true')
my_parser.add_argument(
    '-e', '--cifradocesar',
    help="Activar modulo CifradoCesar",
    action='store_true')
my_parser.add_argument(
    '-d', '--descifrado',
    help="Activar modulo Descifrado",
    action='store_true')
my_parser.add_argument(
    '-s', '--escaneo',
    help="Activar modulo Escaneo de Red",
    action='store_true')
my_parser.add_argument(
    '-m', '--metadata',
    help="Activar modulo metadata",
    action='store_true')
my_parser.add_argument(
    '-b', '--brute',
    help="Activar modulo bruteforce",
    action='store_true')
my_parser.add_argument(
    '-f', '--force',
    help="Fuerza la ejecucion de todos los modulos. (excepto bruteforce)",
    action='store_true')

with open("config.json", "r") as f:
    data = json.load(f)
    de = data["enviocorreo"]["de"]
    para = data["enviocorreo"]["para"]
    asunto = data["enviocorreo"]["asunto"]
    clave = data["enviocorreo"]["clave"]
    txtfrasetoU = data["cifrado"]["txtfrasetoU"]
    txtfrasetoD = data["cifrado"]["txtfrasetoD"]
    txtfrasetoC = data["cifrado"]["txtfrasetoC"]
    user = data["bruteforce"]["user"]
    passfile = data["bruteforce"]["passfile"]
    url = data["bruteforce"]["url"]

logging.info('Variables cargadas desde config.json')


def main():

    print("--------------PIA PROGRAMACION PARA CIBERSEGURIDAD--------------")

    if ((args.web is False and args.enviocorreo is False and
         args.cifradocesar is False and args.descifrado is False and
            args.escaneo is False and args.metadata is False) and (
            args.force is not True)):
        logging.info('Finalizacion de programa debido a falta de argumentos.')
        print('El programa no puede continuar si no se le han '
              'asignado modulos a activar.')
        print('Porfavor, digite "py PIA.py -h", para asi '
              'poder ver que modulos puede activar :) ')
        sys.exit()

    # WEB SCRAPING
    if args.web is True or args.force is True:
        logging.info('Iniciando operacion WEB SCRAPPING')
        print("Iniciando operacion WEB SCRAPING")
        try:
            webscrap.noticias()
        except Exception as e:
            print("""ERROR, NO SE PUDO COMPLETAR CORRECTAMENTE
                    ,LA OPERACION,CODIGO: """ + e.text)
            logging.info('Error en la operacion WEB CRAPPING: ' + e.text)
        else:
            print("Operacion WEB SCRAPING finalizada con exito")
            logging.info('Operacion webscrap finalizada con exito')

    # ESCANEO DE PUERTOS
    if args.escaneo is True or args.force is True:
        logging.info('Iniciando operacion escaneo de puertos')
        print("Iniciando operacion ESCANEO DE PUERTOS")
        try:
            escan.escan_ports()
        except Exception as e:
            print("""ERROR, NO SE PUDO COMPLETAR CORRECTAMENTE
                    ,LA OPERACION,CODIGO: """ + e.text)
            logging.info('Error en la operacion PORTSCAN: ' + e.text)
        else:
            print("Operacion escanneo de puertos finalizada con exito")
            logging.info('Operacion PORTSCAN finalizada con exito')

    # ENVIO CORREOS
    if ((args.escaneo is False and args.web is False and args.enviocorreo
            is True) and (args.force is not True)):
        print("Este modulo necesita que este activo almenos uno de los"
              "siguientes modulos:\n"
              "1.-Escaneo de puertos\n"
              "2.-WebScrapping\n"
              "Esto debido, a que este modulo envia los resultados de uno"
              " o ambos de los modulos anteriores")
        logging.info(
            'Finalizacion del programa por la falta de datos de otros '
            'modulos')
        sys.exit()
    elif args.enviocorreo is True or args.force is True:
        print("Iniciando operacion ENVIO CORREOS")
        logging.info('Iniciando operacion ENVIO CORREOS')
        try:
            correo.enviarcorreo(de, para, asunto, clave)
        except Exception as e:
            logging.info('Error en la operacion ENVIOCORREOS' + e.text)
            print("""ERROR, NO SE PUDO COMPLETAR CORRECTAMENTE
                    ,LA OPERACION,CODIGO: """ + e.text)
        else:
            print("Operacion ENVIO CORREOS finalizada con exito")
            logging.info('Operacion envio correos finalizada con exito')

    # CIFRADO
    if ((args.escaneo is False and args.cifradocesar is True) and (
            args.force is not True)):
        print("Este modulo necesita que este activo uno de los"
              "siguientes modulos:\n"
              "1.-Escaneo de puertos\n"
              "Esto debido, a que este modulo trabaja con los resultados "
              "de los modulos anteriores.")
        logging.info('Finalizacion del programa por la falta de datos de otros'
                     'modulos')
        sys.exit()
    elif args.cifradocesar is True or args.force is True:
        t = open(txtfrasetoU, 'r', errors="ignore")
        texto = t.read()
        t.close()
        logging.info('Iniciando operacion CIFRADO CESAR')
        print("Iniciando operacion CIFRADO CESAR")
        try:
            frasec = cifrado.Encriptar(texto)
            f = open(txtfrasetoC, 'w', errors="ignore")
            f.write(frasec)
            f.close
        except Exception as e:
            logging.info('Error en la operacion CIFRADOCESAR' + e.text)
            print("""ERROR, NO SE PUDO COMPLETAR CORRECTAMENTE
                    ,LA OPERACION,CODIGO: """ + e.text)
        else:
            print("Operacion CIFRADO CESAR finalizada con exito")
            logging.info('Operacion CIFRADO CESAR FINALIZADA CON EXITO')

    # DESCIFRADO
    if (args.escaneo is False and args.cifradocesar is False
            and args.descifrado is True and args.force is not True):
        print("Este modulo necesita que este activo uno de los"
              "siguientes modulos:\n"
              "1.-Escaneo de puertos\n"
              "2.-Cifrado Cesar\n"
              "Esto debido, a que este modulo trabaja con los resultados "
              "de los modulos anteriores.")
        logging.info('Finalizacion del programa por la falta de datos de otros'
                     'modulos')
        sys.exit()
    elif args.descifrado is True or args.force is True:
        print("Iniciando operacion DESCIFRADO CESAR")
        logging.info('Iniciando operacion DESCIFRADO CESAR')
        try:
            frased = desci.Desencriptar(frasec)
            frased = desci.Desencriptar(frased)
            f = open(txtfrasetoD, 'w', errors="ignore")
            f.write(frased)
            f.close
        except Exception as e:
            logging.info('Error en la operacion DESCIFRADO CESAR' + e.text)
            print("""ERROR, NO SE PUDO COMPLETAR CORRECTAMENTE
                    ,LA OPERACION,CODIGO: """ + e.text)
        else:
            logging.info('Operacion DESCIFRADO CESAR finalizada con exito')
            print("Operacion DESCIFRADO CESAR finalizada con exito")

    # METADATA
    if (args.escaneo is False and args.web is False
            and args.force is not True):
        print("Este modulo necesita que este activo uno de los"
              "siguientes modulos:\n"
              "1.-Escaneo de puertos\n"
              "2.-Web Scrapping\n"
              "Esto debido, a que este modulo trabaja con los resultados "
              "de los modulos anteriores.")
        logging.info('Finalizacion del programa por la falta de datos de otros'
                     'modulos')
        sys.exit()
    elif args.metadata is True or args.force is True:
        print("Iniciando operacion METADATA")
        logging.info('Iniciando operacion METADATA')
        try:
            meta.printMeta()
        except Exception as e:
            logging.info('Error en la operacion METADATA' + e.text)
            print("""ERROR, NO SE PUDO COMPLETAR CORRECTAMENTE
                    ,METADATA ,CODIGO: """ + e.text)
        else:
            logging.info('Operacion METADATA finalizada con exito')
            print("Operacion METADATA finalizada con exito")

    # BRUTEFORCE
    if (args.brute is True):
        print("Iniciando operacion BRUTEFORCE")
        logging.info('Iniciando operacion BRUTEFORCE')
        try:
            brutef.bruteforce(user, passfile, url)
        except Exception as e:
            logging('Error en la operacion BRUTEFORCE' + e.text)
            print("Error en la operacion BRUTEFORCE" + e.text)
        else:
            logging.info("Operacion BRUTEFORCE finalizada con exito")
            print("Operacion BRUTEFORCE finalizada con exito")


if __name__ == "__main__":
    args = my_parser.parse_args()
    logging.info('Parseo de argumentos')
    if args.force is True:
        logging.info('Argumento FORCE activado')
    logging.info('Inicializacion de la funcion main()')
    main()
    print("Fin")
    logging.info('Fin del programa')
