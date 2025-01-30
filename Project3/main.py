#Rules of game
# Rock beats Scissors
# Rock smashes scissors, so Rock wins.

# Scissors beat Paper
# Scissors cut paper, so Scissors win.

# Paper beats Rock
# Paper covers rock, so Paper wins.

# Same choice results in a draw
# If both players choose the same option (Rock vs Rock, Paper vs Paper, etc.), it’s a tie.


import random 

computer = ["Rock", "Paper", "Scissors"]
print(computer)
total_won = 0
total_lost = 0
total_tied = 0
game = int(input('Enter game here: '))
for i in range(game):
    computer_choice = random.choice(computer)
    user_Chose = input("Chose on of it: Rock, Paper or Scissors (Exit): ").capitalize()
    if user_Chose == 'Rock' and computer_choice == 'Scissors':
        print(f"computer chose {computer_choice} and you chose {user_Chose}:\nYou won")
        total_won += 1
        print(f"You won total games: {total_won}")

    elif user_Chose == 'Scissors' and computer_choice == 'Paper':
        print(f"computer chose {computer_choice} and you chose {user_Chose}:\nYou won")
        total_won += 1
        print(f"You won total games: {total_won}")

    elif user_Chose == 'Paper' and computer_choice == "Rock" or user_Chose == 'paper':
        print(f"computer chose {computer_choice} and you chose {user_Chose}:\nYou won")
        total_won += 1
        print(f"You won total games: {total_won}")

    elif computer_choice == 'Rock' and user_Chose == 'Scissors':
        print(f"Computer chose {computer_choice} and you chose {user_Chose}:\n You lost !")
        total_lost += 1
        print(f"You lost total games: {total_lost}")
    
    elif computer_choice == 'Scissors' and user_Chose == 'Paper':
        print(f"Computer chose {computer_choice} and you chose {user_Chose}:\n You lost !")
        total_lost += 1
        print(f"You lost total games: {total_lost}")

    elif computer_choice == 'Paper' and user_Chose == "Rock":
        print(f"Computer chose {computer_choice} and you chose {user_Chose}:\n You lost !")
        total_lost += 1
        print(f"You lost total games: {total_lost}")

    elif user_Chose == "exit":
        print("game end! thank you for playing")
        break
    elif user_Chose == computer_choice:
        print(f"computer chose: {computer_choice} and you chose: {user_Chose}: Match Tied")
        total_tied += 1
    
if total_won > total_lost:
    print("Congratulation You won")

elif total_won < total_lost:
    print("You lost ! Better luck next time.")
else:
    print("Match tied! ")
print(f"Your Final Result:\nWon: {total_won}\nLost: {total_lost}\nTied:{total_tied}")


