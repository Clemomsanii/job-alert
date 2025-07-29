def match_jobs(jobs, skills):
    matched = []
    for job in jobs:
        for skill in skills:
            if skill.lower() in job["title"].lower():
                matched.append(job)
                break
    return matched