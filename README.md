# WoW Forever Level 60 Characters Table

Web app that scrapes public armory data for **World of Warcraft: Forever** (the official permanent level-60 classic experience), filters characters that are level 60, and displays them in a searchable/filterable table.

## Important Notes

- Blizzard's official Battle.net / WoW API **does not provide a list or search of all characters**. You can only query a character if you already know its name (first + surname) and it is level 10+.
- This project therefore scrapes public third-party armories (primarily [aotc.gg/forever](https://www.aotc.gg/forever) leaderboards and character pages) that have already collected data via individual lookups.
- Leaderboards on third-party sites are mostly high-end (level 60) characters ranked by Gear Score, Item Level, etc.
- Data is public and for informational purposes. Respect rate limits and the sites' terms of service.

## Features (planned / starter)

- Scrape gear score / item level leaderboards
- Extract character name, region, ruleset, class, guild, gear score
- Filter only level 60 (or verify level by fetching profile if needed)
- Display in a clean HTML table with search and filters (region, class, ruleset)
- Refresh button / scheduled scrape

## Tech Stack (starter)

- Python 3 + Flask
- requests + BeautifulSoup4 for scraping
- Simple HTML/CSS/JS frontend

## Setup

```bash
git clone https://github.com/SSC92/wow-forever-level60-table.git
cd wow-forever-level60-table
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Next Steps

- Add more sources (armorywowforever.com, etc.)
- Cache results in SQLite
- Add character detail pages
- Deploy (Vercel, Railway, etc.)

Contributions welcome!
