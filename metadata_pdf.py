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
            ruta = os.getcwd()
            os.chdir(ruta)
            # Un for para iterar cada archivo de la carpeta
            for root, dirs, files in os.walk(".", topdown=False):
                for name in files:
                    ext = name.lower() .rsplit('.', 1)[-1]
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
            os.remove('./prueba1.ps')

    except OSError:
        print("Tu sistema es operativo es Windows, "
              "no se ejecutara el modulo METADATA")


printMeta()
