\# Air \& Space Force Enlisted Jobs Finder



A web app that provides up-to-date information on \*\*enlisted jobs\*\* in the \*\*Air Force\*\* and \*\*Space Force\*\*.  

Data is scraped weekly from official sites and merged into a searchable, filterable React app.



\## 🚀 Features

\- Live data scrapers for Air Force \& Space Force career sites

\- Space Force crosswalk parser (AFSC → SF equivalents)

\- React + Tailwind frontend with search and job detail views

\- Styled with a military/space aesthetic

\- GitHub Actions auto-update jobs.json weekly



\## 📂 Structure

\- `frontend/` → React app (Vite + Tailwind)

\- `scraper/` → Python scrapers \& merger

\- `data/` → intermediate + final jobs.json

\- `.github/workflows/` → auto-update workflow



\## 🛠 Setup

```bash

\# Install frontend

cd frontend

npm install

npm run dev



\# Run scrapers (from repo root)

cd scraper

pip install requests beautifulsoup4 pdfplumber

python af\_scraper.py

python sf\_scraper.py

python crosswalk\_parser.py   # requires crosswalk PDF in /data

python build\_jobs.py



