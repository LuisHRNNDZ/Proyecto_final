from PyPDF2 import PdfFileReader


pdfFileObj = open('teoria-de-automatas-y-lenguajes-formales-dean-kelley_compress.pdf', 'rb')
pdf = PdfFileReader(pdfFileObj)
print("Páginas: ", pdf.getNumPages())
print("Título: ", pdf.documentInfo.title)
print("Pagina: ", pdf.getPage(12))
primera_hoja = pdf.getPage(0)
print(primera_hoja.extractText())

