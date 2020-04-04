import scrapper
import smtplib, ssl
import firebase_conf


def get_message():
    return """\
    Subject: COVID-19 daily

    {}
    {}
    """.format(scrapper.get_world_data(), scrapper.get_pl_data())


def send_notifications(sender_email: str, sender_pwd: str):
    print("Trying to sending daily notifications")

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = sender_email
    receivers = firebase_conf.get_receiver_emails()
    password = sender_pwd
    message = get_message()

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)

        counter = 0
        for receiver_email in receivers:
            server.sendmail(sender_email, receiver_email, message)
            counter += 1

        print("Emails sent to {} addresses".format(str(counter)))
