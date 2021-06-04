import random

options = ["rock", "paper", "scissor"]

def get_pc_guess():
    return random.choice(options)

def get_user_guess():
    return input("Rock, Paper or Scissor? \nEnter: ")

def user_guess_valid(guess):
    if type(guess) == str and guess.lower() in options:
        return True
    else:
        return False

def get_winner(user, pc):

    if user == "rock" and pc == "scissor" or user == "paper" and pc == "rock" or user == "scissor" and pc == "rock":
        return "user", user, "pc", pc
    
    return "pc", pc, "user", user


def main():

    while True:

        print("----------------------------")
        pc_guess = get_pc_guess()
        stop = False

        while not stop:

            user_guess = get_user_guess()

            if user_guess_valid(user_guess):
                break

            print(f"---> {user_guess} is not a valid guess")
            if input("Try again? \n[no] \n[yes] \nEnter: ") == "no":
                stop = True

        if stop:
            break

        if user_guess == pc_guess:
            print("It's a tie!")
        else:
            winner, winner_guess, loser, loser_guess = get_winner(user_guess, pc_guess)
            print(f"---> {winner}'s {winner_guess} won against {loser}'s {loser_guess}")
        
        if input("Play again? \n[no] \n[yes] \nEnter: ") == "no":
            break

    print("---------------------------- \nExited the game!")

main()