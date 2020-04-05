import schedule
import time
from email_utils import email_client
import firebase_conf

print("Starting covid-scheduler application")

# Initialize firebase configuratiom
firebase_conf.init_firebase()

# Get email_utils address and password of mail sender
# sender_email = input('Enter sender email:')
# sender_pwd = input('Enter sender password:')
sender_email = 'covid.informator@gmail.com'
sender_pwd = 'nq,}b6nCZ)y=J\,6'


def job():
    print("Starting scheduled job")
    email_client.send_notifications(sender_email, sender_pwd)


# Schedule request
schedule.every().day.at("10:55").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
