import smtplib, ssl
import firebase_conf
from email.mime.text import MIMEText
from email_utils import mail_template


def send_notifications(sender_email: str, sender_pwd: str):
    print("Trying to sending daily notifications")

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = sender_email
    receivers = firebase_conf.get_receiver_emails()
    password = sender_pwd
    message = mail_template.get_mail_template()

    my_email = MIMEText(message, "html")
    my_email["From"] = sender_email
    my_email["Subject"] = "COVID-19 summary"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)

        counter = 0
        for receiver_email in receivers:
            my_email["To"] = receiver_email

            server.sendmail(sender_email, receiver_email, my_email.as_string())
            counter += 1

        print("Emails sent to {} addresses".format(str(counter)))
