def send_email(jobs, receiver_email):
    if not jobs:
        print("No matching jobs found.")
        return
    print(f"Sending email to {receiver_email} with {len(jobs)} job(s)...")
    for job in jobs:
        print(f"- {job['title']} at {job['company']} ({job['method']} application): {job['link']}")