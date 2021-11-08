from PyPDF2 import PdfFileReader
import os
import subprocess


# definiendo la funcion
def printMeta():
    # Intenta correr el script, si no corre es debido a que es windows.
    try:
        document = "./metadata.txt"
        # Abre documento
        with open(document, 'w', errors="ignore") as f:
            # Manda a llamar a el script de bash
            subprocess.call('./converter_pdf.sh')
            # guarda la ruta actual en la variable ruta
            ruta = os.getcwd()
            # choosedir / cambia al directorio actual en caso de que estes en otro
            os.chdir(ruta)
            # Un for para iterar cada archivo de la carpeta
            for root, dirs, files in os.walk(".", topdown=False):
                # Un for para iterar los nombres de las carpetas
                for name in files:
                    # ext = nombre del archivo en minusculas
                    ext = name.lower() .rsplit('.', 1)[-1]
                    # por cada archivo que termine en pdf
                    if ext in ['pdf']:
                        # imprime metadata
                        f.write("[+] Metadata for file: %s " %
                                (ruta + os.path.sep + name) + "\n")
                        pdfFile = PdfFileReader(
                            open(ruta + os.path.sep + name, 'rb'))
                        docInfo = pdfFile.getDocumentInfo()
                        f.write("Tipo: " + str(type(docInfo)) + "\n")
                        for metaItem in docInfo:
                            f.write('[+] ' + metaItem + ':' +
                                    docInfo[metaItem] + "\n")
                        f.write("\n")
            # remueve prueba1.ps 
            os.remove('./prueba1.ps')

    # Windows
    except OSError:
        print("Tu sistema es operativo es Windows, "
              "no se ejecutara el modulo METADATA")


printMeta()
