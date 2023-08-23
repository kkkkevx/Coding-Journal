# Write your code here.

def get_number_of_teams():
    num_teams = int(input("Enter the number of teams in the tournament: "))

    while num_teams < 2:
        print(f"The minimum Number of teams is 2, try again.")
        num_teams = int(input("Enter the number of teams in the tournament: "))

    return num_teams


def get_team_names(num_teams):
    team_list = []
    for i in range(1, num_teams+1):
        team_name = input(f"Enter the name for team #{i}: ")
        while len(team_name) < 2:
            print("Team names must have at least 2 characters, try again.")
            team_name = input(f"Enter the name for team #{i}: ")
        while len(team_name.split()) > 2:
            print("Team names may have at most 2 words, try again.")
            team_name = input(f"Enter the name for team #{i}: ")
        team_list.append([team_name, 0])
    return team_list

        


def get_number_of_games_played(num_teams):
    numb_game_play = int(input("Enter the number of games played by each team: "))
    while True:
        if numb_game_play >= (num_teams - 1):
            break
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        numb_game_play = int(input("Enter the number of games played by each team: "))
    return numb_game_play



def get_team_wins(team_names, games_played):
    for i in team_names:
        while True:
            numb_of_win = int(input(f"Enter the number of wins Team {i[0]} had: "))
            if numb_of_win < 0:
                print("The minimum number of wins is 0, try again.")
            elif numb_of_win > games_played:
                print(f"The maximum number of wins is {games_played}, try again")
            else:
                i[1] = numb_of_win
                break
    return team_names
# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)


print("Generating the games to be played in the first round of the tournament...")
team_wins.sort(key= lambda x: x[1])
j = -1
for i in range(num_teams//2):
    print(f"Home: {team_wins[i][0]} VS Away: {team_wins[j][0]}")
    j -= 1