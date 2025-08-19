import json, os

def load(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return []

af = load("../data/airforce.json")
sf = load("../data/spaceforce.json")
crosswalk = load("../data/crosswalk.json")

# merge AF + SF, enrich with crosswalk if codes match
jobs = af + sf
for job in jobs:
    for row in crosswalk:
        if job.get("code") and row["afsc"] == job["code"]:
            job["mapped_title"] = row["sf_title"]

with open("../frontend/public/data/jobs.json", "w") as f:
    json.dump(jobs, f, indent=2)

print(f"✅ Final jobs.json with {len(jobs)} jobs")
