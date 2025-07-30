# main.py

from config import EMAIL_RECEIVER
from utils.notifier import send_email

# Dummy jobs to simulate matches
dummy_jobs = [
    {
        "title": "Python Developer",
        "link": "https://example.com/job/python-dev",
        "location": "Nairobi"
    },
    {
        "title": "Data Analyst",
        "link": "https://example.com/job/data-analyst",
        "location": "Remote"
    }
]

if __name__ == "__main__":
    send_email(dummy_jobs, EMAIL_RECEIVER)
