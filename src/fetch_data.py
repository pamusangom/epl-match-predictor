import json

with open(r"C:\Users\Pa Musa Ngom\OneDrive\Documents\premier-league-predictor\data\premier_league.json", "r", encoding="utf-8") as f:
    data = json.load(f)

matches = []


for match in data["matches"]:
    home = match["team1"]
    away = match["team2"]
    
    score = match.get("score", {})

    if "ft" in score:
        home_goals = score["ft"][0]
        away_goals = score["ft"][1] 
        played = True
    
    else:
        home_goals = None
        away_goals = None
        played = False

    matches.append({
        "home_team": home,
        "away_team": away,
        "home_goals": home_goals,
        "away_goals": away_goals,
        "played": played
    })

for m in matches[:5]:
    print(m)