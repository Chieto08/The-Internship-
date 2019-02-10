import random

def start_game():
    print(" Welcome to 'THE DICE GAME'. This game involves rolling 2 dices in \n which the player which has the highest score when both scores of the dices rolled \n is calculated, emerges as winner. At least 2 players are required to be active on \n this game, and a maximum of 100 players. Best of luck")
    no_of_players = int(input("How many players are active? "))
    player_playernames = []
    for name in range(no_of_players):
        if no_of_players>= 2 and no_of_players<= 100:
            player_names = input("Enter the name of player " + str(name + 1) + ":" )
            while player_names in player_playernames:
                player_names = input("Enter the name of player " + str(name + 1) + ",name " + player_names + " is taken:" )
            else:
                player_playernames.append(player_names)
        else:
            print("Invalid number of players.")
            exit()
    return player_playernames

def roll_dice(player_playernames):
    player_playernames_and_scores = {}
    for trial in range(3):
        for player in player_playernames:
            roll = input("Hey " + player + " enter 1 to roll a dice: ") 
            while roll != "1":
                roll = input("Hey " + player + ", " + roll + " does not equal 1. Enter 1 to roll a dice: ")      
            else:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print("Results for " + player+ " from trial " + str(trial + 1)+ ": Dice 1: " + str(dice1) + ", Dice 2: " + str(dice2))
                total_score = dice1 + dice2
                if (is_a_valid_key(player_playernames_and_scores,player)) == False:
                    player_playernames_and_scores[player] = []
                    player_playernames_and_scores[player].append(total_score)
                elif (is_a_valid_key(player_playernames_and_scores,player)) == True:
                    player_playernames_and_scores[player].append(total_score)
                
    return player_playernames_and_scores

def get_highest_score(player_playernames_and_scores):
    player_playernames_and_highest_scores = {}
    for player in player_playernames_and_scores:
        player_playernames_and_highest_scores[player] = max(player_playernames_and_scores[player])
    return player_playernames_and_highest_scores

def choose_winner(player_playernames):
    player_playernames_and_scores = roll_dice(player_playernames)
    player_playernames_and_highest_scores = get_highest_score(player_playernames_and_scores)
    maximum_element = 0
    final_winner = ""
    players_max = []
    for value in player_playernames_and_highest_scores.values():
        players_max.append(value)
    maximum_element = max(players_max)
    if check_tie(players_max, maximum_element) == True:
        print("Tied")
        tied_players = get_key(player_playernames_and_highest_scores, maximum_element)
        players_max = []
        resolve_tie(tied_players)
    elif check_tie(players_max, maximum_element) == False:
        the_winner = get_key(player_playernames_and_highest_scores, maximum_element)
        for winner in the_winner:
            final_winner = winner
        return "The winner is " + final_winner + " with a score of " + str(maximum_element)

def check_tie(players_max, maximum_element):
    if players_max.count(maximum_element) > 1:
        return True
    elif players_max.count(maximum_element) == 1:
        return False
 
def resolve_tie(tied_players):
    print("Tie between " + str(tied_players))
    print(choose_winner(tied_players))
    

def get_key(dictionary, val):
     key = [key for key,value in dictionary.items() if value == val]
     return key

def is_a_valid_key(dictionary, player):
    if player in dictionary:
        return True
    else:
        return False

print(choose_winner(start_game()))
