# main.py

from sites import job_sites

def check_jobs():
    for site in job_sites:
        print(f"🔍 Checking for jobs at {site['name']} ({site['url']})...")
        # In future: Add real scraping logic here
        print(f"✅ Done checking {site['name']}.\n")

if __name__ == "__main__":
    check_jobs()
