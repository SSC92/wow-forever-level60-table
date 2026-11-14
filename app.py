from flask import Flask, render_template, jsonify
from scraper import scrape_aotc_gearscore

app = Flask(__name__)

@app.route("/")
def index():
    characters = scrape_aotc_gearscore(limit=100)
    return render_template("index.html", characters=characters)

@app.route("/api/characters")
def api_characters():
    characters = scrape_aotc_gearscore(limit=100)
    return jsonify(characters)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
