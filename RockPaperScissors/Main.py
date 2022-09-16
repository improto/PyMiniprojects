import random

def play():
    user_choice = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        return 'Its a Tie'

    if its_a_win(user_choice, computer_choice):
        return 'You win'

    return 'You lost'

        #r > s , p > r , s > p

def its_a_win(player, opponent):
    #Returns True if player wins

    if (player == 'r' and opponent == 's') or (player == "p" and opponent == "r") or (player == "s" and opponent == "p"):
        return True

play()