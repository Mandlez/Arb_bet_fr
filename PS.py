from bs4 import BeautifulSoup
import requests

competition_urls = {
		'football':
		{
			"ligue1": "https://www.enligne.parionssport.fdj.fr/paris-football/france/ligue-1-uber-eats",
            "ligue2": "https://www.enligne.parionssport.fdj.fr/paris-football/france/ligue-2-bkt",
			"liga": "https://www.enligne.parionssport.fdj.fr/paris-football/espagne/laliga",
            "liga2": "https://www.enligne.parionssport.fdj.fr/paris-football/espagne/laliga-2",
			"bundesliga": "https://www.enligne.parionssport.fdj.fr/paris-football/allemagne/bundesliga-1",
            "bundesliga2": "https://www.enligne.parionssport.fdj.fr/paris-football/allemagne/bundesliga-2",
			"premier-league": "https://www.enligne.parionssport.fdj.fr/paris-football/angleterre/premier-league",
            "championship": "https://www.enligne.parionssport.fdj.fr/paris-football/angleterre/championship",
			"serie-a": "https://www.enligne.parionssport.fdj.fr/paris-football/italie/serie-a",
            "serie-b": "https://www.enligne.parionssport.fdj.fr/paris-football/italie/serie-b",
			"primeira": "https://www.enligne.parionssport.fdj.fr/paris-football/portugal/liga-portugal",
			"serie-a-brasil": "https://www.enligne.parionssport.fdj.fr/paris-football/bresil/d1-bresil",
			"a-league": "https://www.enligne.parionssport.fdj.fr/paris-football/australie/d1-australie",
			"division-1a": "https://www.enligne.parionssport.fdj.fr/paris-football/belgique/d1-belgique",
			"super-lig": "https://www.enligne.parionssport.fdj.fr/paris-football/turquie/d1-turquie",
		},
		'basketball':
		{
			"nba": "https://www.enligne.parionssport.fdj.fr/paris-basketball/usa/nba",
			"euroligue": "https://www.enligne.parionssport.fdj.fr/paris-basketball/international/euroleague-h",
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
    game_elements = html.select(".psel-event")
    games = []
    for el in game_elements:
        names = el.select(".psel-opponent__name")
        team1 = "".join(names[0].text.split())
        team2 = "".join(names[1].text.split())
        odds_els = el.find_all('span', class_='psel-outcome__data')[:3]
        odds = [odd.text.replace(',', '.') for odd in odds_els]  # Remplacez les virgules par des points
        odds = [float(odd) if odd.replace('.', '', 1).isdigit() else odd for odd in odds]

        games.append({
            'team1': team1,
            'team2': team2,
            'odds': odds
    })

    return games