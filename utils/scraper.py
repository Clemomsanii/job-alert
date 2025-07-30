# utils/scraper.py

from sites import job_sites

def scrape_jobs(sites):
    """
    Simulate scraping job data from each site.

    Args:
        sites (list): List of site dictionaries from sites.py.

    Returns:
        list: A list of job posts, each a dict with 'title' and 'description'.
    """
    job_posts = []

    for site in sites:
        print(f"🕸️ Scraping {site['name']}...")

        # Simulated data – replace this with actual scraping logic per site
        job_posts.append({
            "site": site['name'],
            "title": "Software Developer",
            "description": "Looking for a Python developer with web scraping experience."
        })

        job_posts.append({
            "site": site['name'],
            "title": "IT Support Technician",
            "description": "Candidate should be skilled in troubleshooting and networking."
        })

        print(f"✅ Finished scraping {site['name']}.\n")

    return job_posts
