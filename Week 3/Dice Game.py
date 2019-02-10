import random

def start_game():
    print(" Welcome to 'THE DICE GAME'. This game involves rolling 2 dices in \n which the player which has the highest score when both scores of the dices rolled \n is calculated, emerges as winner. At least 2 players are required to be active on \n this game, and a maximum of 100 players. Best of luck")
    no_of_players = int(input("How many players are active? "))
    user_details = []
    for name in range(no_of_players):
        if no_of_players>= 2 and no_of_players<= 100:
            user_names = input("Enter the name of user " + str(name + 1) + ":" )
            while user_names in user_details:
                user_names = input("Enter the name of user " + str(name + 1) + ",name " + user_names + " is taken:" )
            else:
                user_details.append(user_names)
        else:
            print("Invalid number of users.")
            exit()
    return user_details

def roll_dice(user_details):
    user_details_and_scores = {}
    for trial in range(3):
        for user in user_details:
            roll = input("Hey " + user + " enter 1 to roll a dice: ") 
            while roll != "1":
                roll = input("Hey " + user + ", " + roll + " does not equal 1. Enter 1 to roll a dice: ")      
            else:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print("Results for " + user+ " from trial " + str(trial + 1)+ ": Dice 1: " + str(dice1) + ", Dice 2: " + str(dice2))
                total_score = dice1 + dice2
                if (is_a_valid_key(user_details_and_scores,user)) == False:
                    user_details_and_scores[user] = []
                    user_details_and_scores[user].append(total_score)
                elif (is_a_valid_key(user_details_and_scores,user)) == True:
                    user_details_and_scores[user].append(total_score)
                
    return user_details_and_scores

def get_highest_score(user_details_and_scores):
    user_details_and_highest_scores = {}
    for user in user_details_and_scores:
        user_details_and_highest_scores[user] = max(user_details_and_scores[user])
    return user_details_and_highest_scores

def choose_winner(user_details):
    user_details_and_scores = roll_dice(user_details)
    user_details_and_highest_scores = get_highest_score(user_details_and_scores)
    maximum_element = 0
    final_winner = ""
    users_max = []
    for value in user_details_and_highest_scores.values():
        users_max.append(value)
    maximum_element = max(users_max)
    if check_tie(users_max, maximum_element) == True:
        print("Tied")
        tied_users = get_key(user_details_and_highest_scores, maximum_element)
        users_max = []
        resolve_tie(tied_users)
    elif check_tie(users_max, maximum_element) == False:
        the_winner = get_key(user_details_and_highest_scores, maximum_element)
        for winner in the_winner:
            final_winner = winner
        return "The winner is " + final_winner + " with a score of " + str(maximum_element)

def check_tie(users_max, maximum_element):
    if users_max.count(maximum_element) > 1:
        return True
    elif users_max.count(maximum_element) == 1:
        return False
 
def resolve_tie(tied_users):
    print("Tie between " + str(tied_users))
    print(choose_winner(tied_users))
    

def get_key(dictionary, val):
     key = [key for key,value in dictionary.items() if value == val]
     return key

def is_a_valid_key(dictionary, user):
    if user in dictionary:
        return True
    else:
        return False

print(choose_winner(start_game()))
