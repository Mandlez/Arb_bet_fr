import requests
import json

competition_urls = {
		'football':
		{
			"ligue1": "https://www.winamax.fr/paris-sportifs/sports/1/7/4",
        	"ligue2": "https://www.winamax.fr/paris-sportifs/sports/1/7/19",
			"liga": "https://www.winamax.fr/paris-sportifs/sports/1/32/36",
        	"liga2": "https://www.winamax.fr/paris-sportifs/sports/1/32/37",
			"bundesliga": "https://www.winamax.fr/paris-sportifs/sports/1/30/42",
        	"bundesliga2": "https://www.winamax.fr/paris-sportifs/sports/1/30/41",
        	"premier-league": "https://www.winamax.fr/paris-sportifs/sports/1/1/1",
        	"championship": "https://www.winamax.fr/paris-sportifs/sports/1/1/2",
			"serie-a": "https://www.winamax.fr/paris-sportifs/sports/1/31/33",
        	"serie-b": "https://www.winamax.fr/paris-sportifs/sports/1/31/34",
			"primeira": "https://www.winamax.fr/paris-sportifs/sports/1/44/52",
			"serie-a-brasil": "https://www.winamax.fr/paris-sportifs/sports/1/13/83",
			"a-league": "https://www.winamax.fr/paris-sportifs/sports/1/34/144",
			"division-1a": "https://www.winamax.fr/paris-sportifs/sports/1/33/38",
			"super-lig": "https://www.winamax.fr/paris-sportifs/sports/1/46/62",
		},
		'basketball':
		{
			"nba": "https://www.winamax.fr/paris-sportifs/sports/2/15/177",
			"euroligue": "https://www.winamax.fr/paris-sportifs/sports/2/800000034/153",
		}
}

def get_page(competition):
	if (competition["sport"] in competition_urls and competition["competition"] in competition_urls[competition["sport"]]):
		url = competition_urls[competition["sport"]][competition["competition"]]
	else:
		return None
	response = requests.get(url, headers={"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"})
	html = response.text
	return html

def get_json(competition):
	html = get_page(competition)
	split1 = html.split("var PRELOADED_STATE = ")[1]
	split2 = split1.split(";</script>")[0]
	return json.loads(split2)

def get_games(competition):
	games = []
	json = get_json(competition)
	for game in json['matches']:
		if (json['matches'][game]['sportId'] !=1 and json['matches'][game]['tournamentId'] != 4):
			continue
		team1 = json['matches'][game]['competitor1Name']
		team2 = json['matches'][game]['competitor2Name']
		bet_id = json['matches'][game]['mainBetId']
		bet = json['bets'][str(bet_id)]['outcomes']
		if (len(bet) != 3):
			continue
		odds = [
			json['odds'][str(bet[0])],
			json['odds'][str(bet[1])],
			json['odds'][str(bet[2])],
		]
		games.append({
			'team1': team1,
			'team2': team2,
			'odds': odds
		})

	return games