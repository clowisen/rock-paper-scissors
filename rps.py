import random

count = 0
player_score = 0
computer_score = 0

while(count < 3):
    player = input("Pick rock, paper or scissors: ")

    computer = random.choice(["rock", "paper", "scissors"])

    if(player == computer):
        print("you: ", player, " computer: ", computer)
        print("it's a tie")
    elif(player == "rock" and computer == "paper"):
        print("you: ", player, " computer: ", computer)
        count += 1
        computer_score += 1
    elif(player == "rock" and computer == "scissors"):
        print("you: ", player, " computer: ", computer)
        count += 1
        player_score += 1
    elif(player == "paper" and computer == "scissors"):
        print("you: ", player, " computer: ", computer)
        count += 1
        computer_score += 1
    elif(player == "paper" and computer == "rock"):
        print("you: ", player, " computer: ", computer)
        count += 1
        player_score += 1
    elif(player == "scissors" and computer == "paper"):
        print("you: ", player, " computer: ", computer) 
        count += 1
        player_score += 1  
    elif(player == "scissors" and computer == "rock"):
        print("you: ", player, " computer: ", computer)
        count += 1
        computer_score += 1
    else:
        print("Invalid pick! ")

if(player_score > computer_score):
    print("winner: player")
elif(computer_score > player_score):
    print("winner: computer")




