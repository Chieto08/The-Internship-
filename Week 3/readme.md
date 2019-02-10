# DICE GAME

### About
**The dice game is a game which entails 2 - 100 players actively playing at a time. It involves rolling 2 dies, in which the player with the highest total score wins the game after 3 trials. If there exists a tie, then there is a replay till a single winner emerges.**

---
### Below are the functions and what they do:
### *start_game()*
This function starts the game by explaining the rules of the game to the player, and accepting player usernames.

Requires: Nothing.

Returns: usernames of all active players.

### *roll_dice()*
This function performs the task of playing the game. Which is rolling a dice 3 times and matching a players results with the player's usernames.

Requires: usernames of all active players.

Returns: All player usernames, paired with their scores after 3 trials.

### *get_highest_score()*
This function gets the highest score gotten by each player after 3 trials and stores the player's usernames and the corresponding highest score in a dictionary.

Requires: All player usernames, paired with their scores after 3 trials.

Returns: All player usernames, paired with their highest score.

### *choose_winner()*
This function chooses the winner of the game by picking the player with the highest score out of other players.

Requires:The player usernames, All player usernames, paired with their highest score.

Returns: The winner of the game, if there is no tie. 

### *check_tie()*
This function checks if a tie exists at the end of a game by checking if the highest score appears multiple times.

Requires: The highest score of all players.

Returns: True if the highest score appears multipe times, False otherwise.

### *resolve_tie()*
This function resolves the pending tie by replaying the game from scratch.

Requires: The tied players.

Returns: Nothing.

### *get_key()*
This function gets the player's usernames by the player's score.

Requires: All player usernames, paired with their highest score and the player's highest score.

Returns: The player's usernames


### *is_a_valid_key()*
Checks if the player has previously played, if the player has then the new score is appended to the previous ones else a new list is initialized.

Requires: 	The usernamess of all players paired with their scores, and the usernames of the particular player.

Returns: True if the player has played, else False otherwise.



 