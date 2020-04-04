import schedule
import time
from email_utils import email_client
import firebase_conf

print("Starting covid-scheduler application")

# Initialize firebase configuratiom
firebase_conf.init_firebase()

# Get email_utils address and password of mail sender
sender_email = input('Enter sender email:')
sender_pwd = input('Enter sender password:')


def job():
    print("Starting scheduled job")
    email_client.send_notifications(sender_email, sender_pwd)


# Schedule request
# schedule.every(10).seconds.do(job)
schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
