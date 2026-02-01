import json

with open(r"C:\Users\Pa Musa Ngom\OneDrive\Documents\premier-league-predictor\data\premier_league.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for match in data["matches"][:5]:
    home = match["team1"]
    away = match["team2"]
    
    score = match.get("score")

    if score and "ft" in score:
        score1 = score["ft"][0]
        score2 = score["ft"][1] 
    else:
        score1 = "TBD"
        score2 = "TBD"
        
    print(f"{home} vs {away} | Score: {score1}-{score2}")
