
import json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



def enviarcorreo(de,para,asunto,mensaje,clave):

    msg = MIMEMultipart()

    message = mensaje
    password = clave
    msg['From'] = de
    msg['To'] = para
    msg['Subject'] = asunto

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


def uniontxt():
    f= open('./reporte_scan.txt', 'r')
    texto1 = f.read()
    f.close()

    t= open('./noticias.txt', 'r')
    texto2 = t.read()
    t.close()

    texto_unido = '\n\n\n REPORTE SCANNEO DE REDES \n\n\n' + texto1 + '\n\n\n NOTICIAS RECIENTES CIBERSEGURIDAD \n\n\n' + texto2 + '\n\n\n Correo enviado automaticamente PIAPROGRAMACION \n\n\n'

    return texto_unido



de = "prograenviocorreo@gmail.com" # CORREO DESDE EL CUAL SE ENVIARA EL MENSAJE
para = "adrian.cortezcs@uanl.edu.mx,luis.lopezh@uanl.edu.mx,romario.limonhrnd@uanl.edu.mx" # CORREO HACIA DONDE SE ENVIARA EL MENSAJE
asunto = "Prueba" # ASUNTO
mensaje = uniontxt() # MENSAJE 
clave = "enviocorreos.py" # CONTRASEÑA DEL CORREO DESDE EL CUAL SE ENVIARA EL MENSAJE
enviarcorreo(de,para,asunto,mensaje,clave)

