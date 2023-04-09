from dataclasses import dataclass
import numpy as np
from collections import defaultdict

@dataclass
class Team:
    name: str
    wins: int
    draws: int
    losses: int

@dataclass
class League:
    name: str
    total_games: str
    teams: list[Team]

def get_max_games(teams: list[Team], total_games):
	to_simulate_max = 0
	for team in teams:
		to_simulate = total_games - (team.wins + team.losses + team.draws)
		if to_simulate > to_simulate_max:
			to_simulate_max = to_simulate
	return to_simulate

def simulate(teams, max_games, N):
	def get_initial_points(teams):
		points = np.zeros((1, len(teams)))
		for i, team in enumerate(teams):
			points[0, i] = team.wins *3 + team.draws*1
		return points
	
	initial_points = get_initial_points(teams)#(1, teams)
	random_rollout = np.random.uniform(size=(N, len(teams), max_games))

	def get_points(a, prob):
		tick1 = prob[0]
		tick2 = prob[0] + prob[1]
		losses = (a < tick1)
		draws = (np.logical_and(a > tick1, a <tick2))
		wins = (a > tick2)

		return np.sum(losses * 0 + draws * 1 + wins * 3, 2)
	
	total_points = get_points(random_rollout, prob=[1/3]*3) + initial_points#(N, teams)
	winners = np.argmax(total_points, 1)
	unique, counts = np.unique(winners, return_counts=True)
	win_rates = defaultdict(lambda: 0.0)
	for row in np.asarray((unique, counts)).T:
		index, count = row[0], row[1]
		win_rates[teams[index].name] = count/N
		
	return win_rates
				
	
def calculate_probabs(league: League):
    #get max games to simulate
    max_games = get_max_games(league.teams, league.total_games)

    #simulate
    N = 100000
    return simulate(league.teams, max_games, N)
