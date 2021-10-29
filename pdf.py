from PyPDF2 import PdfFileReader


pdfFileObj = open('prueba3.pdf', 'rb')
pdf = PdfFileReader(pdfFileObj)
print("Páginas: ", pdf.getNumPages())
print("Título: ", pdf.documentInfo.title)
print("Pagina: ", pdf.getPage)
primera_hoja = pdf.getPage(0)
print(primera_hoja.extractText())

