import random

while True:
    hands = ['rock', 'paper', 'scissors']

    computer = random.choice(hands)
    player = None

    while player not in hands:
        player = input("Rock, Paper or Scissors: ").lower()

    print("Jogador ", player)
    print("Computer", computer)

    if player == computer:    
        print("Draw")

    elif player == 'rock':
        if computer == 'paper':
            print("Computer Win")
        else:
            print("You Win")

    elif player == 'paper':
        if computer == 'scissors':
            print("Computer Win")
        else:
            print("You Win")

    elif player == 'scissors':
        if computer == 'rock':
            print("Computer Win")
        else:
            print("You Win")

    again = input("Play again? (yes/no) ").lower()

    if again != "yes":
        break
print("Bye")

