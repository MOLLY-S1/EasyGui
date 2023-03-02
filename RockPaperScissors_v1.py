import random, easygui


while True:
    weapons = ["Paper", "Scissors", "Rock"]
    computer = random.choice(weapons)
    welcome = easygui.buttonbox(f"Welcome to Paper, Scissors, Rock\n "
                            f"Do you want to play?", "Welcome",
                            choices= ['Yes', 'No'])
    if welcome == "No":
        break
    else:
        player = easygui.buttonbox("Choose your weapon:", "Weapon Choice",
                                   choices= [weapons[0], weapons[1],
                                             weapons[2]])
        easygui.msgbox(f"You chose {player} and the computer chose {computer}"
                       , "Choices")

        if computer == player:
            result = 'That was a draw'
        elif computer == "Paper" and player == "Rock" or computer == "Scissors" \
                and player == "Paper" or computer == "Rock" and \
                player == "Scissors":
            result = "You lose"
        else:
            result = "You win"
    easygui.msgbox(result)
print("Goodbye")
