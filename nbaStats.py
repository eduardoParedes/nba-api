import requests
from nba_api.stats.static import teams

nba_teams = teams.get_teams()

celtics = [team for team in nba_teams if team['abbreviation'] == 'BOS'][0]
celtics_id = celtics['id']

from nba_api.stats.endpoints import leaguegamefinder

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=celtics_id)

games = gamefinder.get_data_frames()[0]
print(games.head())

# games.groupby(games.SEASON_ID.str[-4:][['GAME_ID']].count().loc['2015':])
