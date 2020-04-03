import schedule
import time
import email_client
import sys

sender_email = sys.argv[1]
sender_pwd = sys.argv[2]


def job():
    email_client.send_mail(sender_email, sender_pwd)


schedule.every(1).seconds.do(job)
schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
