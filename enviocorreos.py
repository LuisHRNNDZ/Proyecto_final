from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Funcion enviar correos


def enviarcorreo(de, para, asunto, clave):
    msg = MIMEMultipart()
    message = uniontxt()  # mensaje a enviar
    password = clave  # password del correo
    msg['From'] = de  # quien envia el correo
    msg['To'] = para  # hacia quien va el correo
    msg['Subject'] = asunto  # el asunto del correo

    # asignamos como texto plano el mensaje.
    msg.attach(MIMEText(message, 'plain'))
    # servidor del correo y puerto desde el que se envia
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # login
    server.login(msg['From'], password)
    # envio de correo, el .split(",") sirve para enviar correo a
    # varios destinatarios.
    server.sendmail(msg['From'], msg['To'].split(","), msg.as_string())
    # close
    server.quit()

# union de los 2 txt los cuales vamos a enviar.


def uniontxt():
    f = open('./reporte_scan.txt', 'r', errors="ignore")
    texto1 = f.read()
    f.close()

    t = open('./noticias.txt', 'r', errors="ignore")
    texto2 = t.read()
    t.close()

    texto_unido = ('\n REPORTE SCANNEO DE REDES \n' + texto1 + '\n\n\n '
                   'NOTICIAS RECIENTES CIBERSEGURIDAD \n\n\n' +
                   texto2 + '\n\n\n Correo enviado automaticamente \n\n\n')

    return texto_unido
