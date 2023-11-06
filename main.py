import Winamax
import Pmu
import config
import Betclic
import PS
import Arbi
import log
import sys
import traceback

# Ajouter la ldc , l'europa ligue et Le rugby

log.init()

progress = 0
for competition in config.competitions:
    progress += 1
    bookmakers = {}
    try:
        bookmakers['winamax'] = Winamax.get_games(competition)
        log.log("winamax: " + str(bookmakers['winamax']))
    except:
        log.log("Cannot crawl winamax: " + traceback.format_exc())
    try:
        bookmakers['Parions-sport'] = PS.get_games(competition)
        log.log("Parions-sport: " + str(bookmakers['Parions-sport']))
    except:
        log.log("Cannot crawl Parions-sport: " + traceback.format_exc())
    try:
        bookmakers['Pmu'] = Pmu.get_games(competition)
        log.log("Pmu: " + str(bookmakers['Pmu']))
    except:
        log.log("Cannot crawl Pmu: " + traceback.format_exc())
    try:
        bookmakers['Betclic'] = Betclic.get_games(competition)
        log.log("Betclic: " + str(bookmakers['Betclic']))
    except:
        log.log("Cannot crawl Betclic: " + traceback.format_exc())


    log.log("-- Competition: {} --".format(competition))


    if 'Winamax' in bookmakers:
        for game in bookmakers['Winamax']:
            games = {}
            for bookmaker in bookmakers:
                try:
                    g = Arbi.get_game(game, bookmakers[bookmaker])
                    if g:
                        games[bookmaker] = g
                except:
                    log.log("Error while retrieving games: {}".format(traceback.format_exc()))
            if (competition["sport"] == "football"):
                Arbi.arb_football(games)
            if (competition["sport"] == "basketball"):
                Arbi.arb_basketball(games)

    print("Progress: {:.2f}%".format(progress / len(config.competitions) * 100))
