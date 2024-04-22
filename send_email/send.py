import os
import dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

dotenv.load_dotenv(override=True)

def send_email(subject, message):
    # Configuration server SMTP Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Port for TLS
    smtp_user = os.getenv("SEND_FROM")
    smtp_password = os.getenv("PASS_SEND_EMAIL") 

    # Creat object MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = os.getenv("SEND_TO")
    msg['Subject'] = subject

    # Adding message to the body e-mail
    msg.attach(MIMEText(message, 'html'))

    try:
        # Starting connection SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)

        # Send e-mail
        server.sendmail(smtp_user, os.getenv("SEND_TO"), msg.as_string())
        print('Send e-mail success', flush=True)
        send_success = True
    except Exception as err:
        print(f'Failed to send e-mail: {err}', flush=True)
        send_success = False
    finally:
        # end connection SMTP
        server.quit()
        return send_success


if __name__ == "__main__":
    # Example
    subject = 'Teste de e-mail'
    message = 'Olá! Este é um teste de e-mail enviado pelo Python.'
    send_email(subject, message)