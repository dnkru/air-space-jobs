import pdfplumber, json, re

PDF_PATH = "../data/spaceforce_crosswalk.pdf"  # download manually first!

def parse_crosswalk(pdf_path=PDF_PATH):
    jobs = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            for line in text.splitlines():
                # Example line: "1N0X1 → Space Operations Specialist"
                match = re.match(r"([0-9A-Z]{2,4}\w*)\s+(.+)", line)
                if match:
                    code, title = match.groups()
                    jobs.append({"afsc": code, "sf_title": title})
    return jobs

if __name__ == "__main__":
    data = parse_crosswalk()
    with open("../data/crosswalk.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Parsed {len(data)} crosswalk entries")
