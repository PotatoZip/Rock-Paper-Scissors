import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Rock, paper or scissors?: ")

    if player == computer:
        print("Computer: {}\nPlayer: {}".format(computer, player))
        print("Tie")
    elif player == "rock":
        if computer == "scissors":
            print("Computer: {}\nPlayer: {}".format(computer, player))
            print("You win!")
        if computer == "paper":
            print("Computer: {}\nPlayer: {}".format(computer, player))
            print("You lose!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: {}\nPlayer: {}".format(computer, player))
            print("You lose!")
        if computer == "rock":
            print("Computer: {}\nPlayer: {}".format(computer, player))
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: {}\nPlayer: {}".format(computer, player))
            print("You lose!")
        if computer == "paper":
            print("Computer: {}\nPlayer: {}".format(computer, player))
            print("You win!")
    play_again = input("Do you want to play again? [Y]")
    if play_again != 'Y':
        print("Bye")
        break