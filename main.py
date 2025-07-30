from utils.scraper import scrape_jobs
from utils.matcher import match_jobs
from utils.notifier import send_email
from config import TARGET_SITES, EMAIL_RECEIVER, SKILLS

def main():
    job_posts = scrape_jobs(TARGET_SITES)
    matched = match_jobs(job_posts, SKILLS)
    send_email(matched, EMAIL_RECEIVER)

if __name__ == "__main__":
    main()
