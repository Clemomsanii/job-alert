# utils/notifier.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import EMAIL_SENDER, EMAIL_PASSWORD

def send_email(jobs, receiver_email):
    if not jobs:
        print("📭 No matching jobs to send.")
        return

    print("📤 Sending email alert...")

    subject = "📌 Weekly Job Matches"
    body = "Here are your matching job postings:\n\n"

    for job in jobs:
        body += f"🔹 {job['title']}\n"
        body += f"🔗 {job['link']}\n"
        body += f"📍 {job['location']}\n\n"

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
            print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
