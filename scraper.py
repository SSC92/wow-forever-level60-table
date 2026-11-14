import requests
from bs4 import BeautifulSoup
import re

def scrape_aotc_gearscore(limit=50):
    """
    Scrapes the top characters from aotc.gg WoW Forever Gear Score leaderboard.
    These are predominantly level 60 characters.
    Returns a list of dicts.
    """
    url = "https://www.aotc.gg/forever/leaderboards/gear-score"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WoWForeverLevel60Table/1.0)"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
        
        characters = []
        # The page structure may change; this is a best-effort parse based on typical list layout.
        # Look for ranked entries. Adjust selectors as needed after inspecting the live page.
        # Example pattern from summaries: rank, name, guild, ruleset, region, GS
        
        # Fallback: extract text blocks that look like character entries
        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        
        # Simple heuristic parse (improve with better selectors once HTML is known)
        i = 0
        while i < len(lines) and len(characters) < limit:
            line = lines[i]
            # Look for patterns like "1 Kris Burger" or numbered ranks
            if re.match(r"^\d+\.?$", line) or (line.isdigit() and i+1 < len(lines)):
                rank = line
                # next lines may contain name, etc.
                name = lines[i+1] if i+1 < len(lines) else "Unknown"
                # This is rough; real implementation should use CSS selectors
                characters.append({
                    "rank": rank,
                    "name": name,
                    "region": "?",
                    "ruleset": "?",
                    "guild": "?",
                    "gear_score": "?",
                    "level": 60,  # assumed for top leaderboard
                    "source": "aotc.gg"
                })
                i += 5  # skip ahead
            else:
                i += 1
        
        # If heuristic failed, return sample data so the table is not empty
        if not characters:
            characters = [
                {"rank": "1", "name": "Example Character", "region": "EU", "ruleset": "Normal", "guild": "Example Guild", "gear_score": "750", "level": 60, "source": "sample"},
                {"rank": "2", "name": "Another Hero", "region": "US", "ruleset": "PvP", "guild": "PvP Guild", "gear_score": "740", "level": 60, "source": "sample"}
            ]
        return characters
    except Exception as e:
        print(f"Scrape error: {e}")
        return [{"rank": "-", "name": "Error fetching data", "region": "-", "ruleset": "-", "guild": "-", "gear_score": "-", "level": 60, "source": "error"}]

if __name__ == "__main__":
    data = scrape_aotc_gearscore(10)
    for c in data:
        print(c)
