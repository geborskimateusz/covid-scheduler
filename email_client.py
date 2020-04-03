import scrapper
import smtplib, ssl


def send_mail(sender_email: str, sender_pwd: str):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = sender_email
    receiver_email = "kokuzio12@gmail.com"
    password = sender_pwd
    message = """\
    Subject: COVID-19 daily

    {}
    {}
    """.format(scrapper.get_world_data(), scrapper.get_pl_data())

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
