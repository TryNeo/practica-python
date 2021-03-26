import smtplib, ssl

def enviarEmail(destinatarios,titulo,contenido):
    port = 465
    password = input("ingrese contraseña:")
    author = "cuentapruebaccs@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(author, password)
        server.sendmail(destinatarios,author,contenido)


def main():
    destinatarios = input("Destinarios:").split()
    title_message = input("Titulo del correo:")
    contenido = input("Contenido:")
    if len(title_message) > 30:
        enviarEmail(destinatarios,title_message,contenido)
    else:
        print("Error el titulo debe ser mayor de 30 caracteres")

if __name__ == "__main__":
    main()