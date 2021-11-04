from PyPDF2 import PdfFileReader
import os
import subprocess


def printMeta():
    try:
        document = "./metadata.txt"
        with open(document, 'w', errors="ignore") as f:
            subprocess.call('./converter_pdf.sh')
            ruta = os.getcwd()
            os.chdir(ruta)
            for root, dirs, files in os.walk(".", topdown=False):
                for name in files:
                    ext = name.lower() .rsplit('.', 1)[-1]
                    if ext in ['pdf']:
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
