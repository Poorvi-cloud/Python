# stone paper scissor

# the simple method to make this:

import random
def sps():
    player_choice = input("enter the choice (stone, paper, scissor)")
    computer_choice = random.choice(["stone", "paper", "scissor"])

    print(f"you choose {player_choice} and computer choose {computer_choice}")

    if player_choice == computer_choice:
        print(" the game is draw")
    elif player_choice == "stone" and computer_choice == "scissor":
        print(" you won !!")
    elif player_choice == "scissor" and computer_choice == "paper":   
        print(" you won !!")
    elif player_choice == "paper" and computer_choice == "stone":
        print(" you won")
    else:
        print("you lose !!!!!!!!!!!")
sps()         