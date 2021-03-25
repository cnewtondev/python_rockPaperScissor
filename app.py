import random
list = ['rock', 'paper', 'scissors']
cpuChoice = random.choices(list)
playChoice = input("Choose rock, paper, or scissors: ")


if cpuChoice[0] == 'rock' and playChoice == 'scissors':
    print("CPU Wins! Rock beats scissors")
elif cpuChoice[0] == 'paper' and playChoice == 'rock':
    print("CPU Wins! Paper beats Rock!")
elif cpuChoice[0] == 'scissors' and playChoice == 'paper':
    print("CPU Wins! Scissors beats Paper!")
elif cpuChoice[0] == playChoice:
    print("It's a draw! " + cpuChoice[0] + " is equal to " + playChoice)
else:
    print("Player Wins! " + playChoice + " beats " + cpuChoice[0] + "!")

