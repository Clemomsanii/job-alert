# utils/matcher.py

def match_jobs(job_posts, skills):
    """
    Filter job posts that match the given skillset.

    Args:
        job_posts (list): List of job descriptions or titles.
        skills (list): List of skills to match against.

    Returns:
        list: Filtered job posts containing any of the skills.
    """
    matched = []

    for job in job_posts:
        combined_text = (job.get("title", "") + " " + job.get("description", "")).lower()
        if any(skill.lower() in combined_text for skill in skills):
            matched.append(job)

    return matched
