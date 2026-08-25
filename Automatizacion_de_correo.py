import smtplib
from os import getenv 
from dotenv import load_dotenv
from email.mime.text import MIMEText
import csv
import sys

# Cargar variables de entorno
load_dotenv()

# variables
remitente = getenv("REMITENTE")
contraseña = getenv("GOOGLE_PASS")
destinatario = []
posibles_nombres = ["correo", "email", "mail", "e-mail", "correo electronico", "correo electrónico"]
n = 0
asunto = "Prueba de automatización"
cuerpo = "¡Hola! Este correo fue enviado automáticamente con Python."

# Lectura de CSV
try:
    with open("CorreosPrueba.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        for encabezado in header:
            if encabezado.casefold() in posibles_nombres:
                break
            n += 1

            try:
                if n == len(header):
                    print("Fila no encontrada")
                    n = abs(int(input("Ingrese el nombre de la fila: ")))
                    if n <= (len(header)) and n != 0:
                        n -= 1
                    else:
                        print("Escriba numeros mayores a 0. Vuelva a iniciar el programa.")
                        sys.exit()        
                    break
            except Exception as e:
                print(f"Debe ser solo numeros, no use caracteres especiales, letas o palabras. {e}")
                sys.exit()

        for row in reader:
            destinatario.append(row[n])
except Exception as e:
    print(f"No existe el archivo. {e}")
    sys.exit()

# Verificación de credenciales y destinatarios
if remitente is None or contraseña is None or len(destinatario) == 0:
    raise ValueError("Faltan las credenciales de correo en las variables de entorno")

# configuración
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remitente, contraseña)

        for row in destinatario:
            mensaje = MIMEText(cuerpo)
            mensaje["Subject"] = asunto
            mensaje["From"] = remitente
            mensaje["To"] = row
            servidor.sendmail(remitente, row, mensaje.as_string())
        print("Correo enviado con éxito")
except smtplib.SMTPAuthenticationError:
    print("Error de autenticación: Verifica tu correo y contraseña de aplicación.")
except smtplib.SMTPRecipientsRefused:
    print("Destinatarios rechazados. Revise la columna seleccionada.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
