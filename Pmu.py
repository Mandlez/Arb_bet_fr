from bs4 import BeautifulSoup
import requests

competition_urls = {
	    'football':
	    {
		    "ligue1": "https://paris-sportifs.pmu.fr/pari/competition/169/football/ligue-1-uber-eats®",
            "ligue2": "https://paris-sportifs.pmu.fr/pari/competition/170/football/ligue-2-bkt®",
		    "liga": "https://paris-sportifs.pmu.fr/pari/competition/322/football/la-liga",
            "liga2": "https://paris-sportifs.pmu.fr/pari/competition/319/football/laliga-2",
		    "bundesliga": "https://paris-sportifs.pmu.fr/pari/competition/32/football/bundesliga",
            "bundesliga2": "https://paris-sportifs.pmu.fr/pari/competition/33/football/bundesliga-ii",
		    "premier-league": "https://paris-sportifs.pmu.fr/pari/competition/13/football/premier-league",
            "championship" : "https://paris-sportifs.pmu.fr/pari/competition/1510/football/championship",
		    "serie-a": "https://paris-sportifs.pmu.fr/pari/competition/308/football/italie-série-a",
            "serie-b": "https://paris-sportifs.pmu.fr/pari/competition/309/football/italie-série-b",
		    "primeira": "https://paris-sportifs.pmu.fr/pari/competition/273/football/primeira-liga",
		    "serie-a-brasil": "https://paris-sportifs.pmu.fr/pari/competition/1779/football/série",
		    "a-league": "https://paris-sportifs.pmu.fr/pari/competition/1812/football/australie-league-h",
		    "division-1a": "https://paris-sportifs.pmu.fr/pari/competition/8124/football/division-1a",
		    "super-lig": "https://paris-sportifs.pmu.fr/pari/competition/1529/football/turquie-super-ligue",
	    },
	    'basketball':
	    {
		    "nba": "https://paris-sportifs.pmu.fr/pari/competition/3502/basket-us/nba",
		    "euroligue": "https://paris-sportifs.pmu.fr/pari/competition/1402/basket-euro/euroligue",
	    }
    }

def get_page(competition):
        if (competition["sport"] in competition_urls and competition["competition"] in competition_urls[competition["sport"]]):
            url = competition_urls[competition["sport"]][competition["competition"]]
        else:
                return None
        response = requests.get(url, headers={"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"})
        html = BeautifulSoup(response.content, 'html.parser')
        return html

def get_games(competition):
    html = get_page(competition)
    game_elements = html.select(".pmu-event-list-grid-highlights-formatter-row")
    games = []
    for el in game_elements:
        game_name = el.select(".trow--event--name")[0].text
        game_name = "".join(game_name.split())
        team1, team2 = game_name.split("//")  # Adjust the delimiter as needed
        odds_el = el.select(".hierarchy-outcome-price")
        odds = []
        for el2 in odds_el:
            tmp = "".join(el2.text.split()).replace(",", ".")
            odds.append(float(tmp))

        games.append({
            'team1': team1,
            'team2': team2,
            'odds': odds
        })

    return games


