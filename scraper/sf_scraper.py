import requests, json
from bs4 import BeautifulSoup

BASE_URL = "https://www.spaceforce.com/career-finder?enlisted=true"

def scrape_spaceforce_jobs():
    resp = requests.get(BASE_URL, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    jobs = []
    for card in soup.select(".career-card"):
        title = card.select_one(".career-card-title")
        summary = card.select_one(".career-card-desc")
        link = card.find("a", href=True)

        jobs.append({
            "service": "Space Force",
            "code": None,
            "title": title.get_text(strip=True) if title else "Unknown",
            "summary": summary.get_text(strip=True) if summary else "",
            "url": "https://www.spaceforce.com" + link["href"] if link else None
        })
    return jobs

if __name__ == "__main__":
    jobs = scrape_spaceforce_jobs()
    with open("../data/spaceforce.json", "w") as f:
        json.dump(jobs, f, indent=2)
    print(f"✅ Saved {len(jobs)} Space Force jobs")
