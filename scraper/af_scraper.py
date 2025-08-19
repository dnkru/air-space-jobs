import requests, json
from bs4 import BeautifulSoup

BASE_URL = "https://www.airforce.com/careers/career-finder?enlisted=true"

def scrape_airforce_jobs():
    resp = requests.get(BASE_URL, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    jobs = []
    for card in soup.select(".career-card"):
        title = card.select_one(".career-card-title")
        summary = card.select_one(".career-card-desc")
        link = card.find("a", href=True)

        jobs.append({
            "service": "Air Force",
            "code": None,  # can enrich later from AFSC mapping
            "title": title.get_text(strip=True) if title else "Unknown",
            "summary": summary.get_text(strip=True) if summary else "",
            "url": "https://www.airforce.com" + link["href"] if link else None
        })
    return jobs

if __name__ == "__main__":
    jobs = scrape_airforce_jobs()
    with open("../data/airforce.json", "w") as f:
        json.dump(jobs, f, indent=2)
    print(f"✅ Saved {len(jobs)} Air Force jobs")
