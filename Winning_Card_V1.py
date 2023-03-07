import random
import easygui

numbers = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
suits = ["Clubs","Diamonds","Hearts","Spades"]

play = easygui.buttonbox("Would you like to play?", "Welcome",
                         choices= ["Yes","No"])
while play == "Yes":

    computer_num = random.choice(numbers)
    computer_suit = random.choice(suits)

    player_num = random.choice(numbers)
    player_suit = random.choice(suits)

    easygui.msgbox(f"The computer drew the {computer_num} of {computer_suit} "
                   f"while the player drew the {player_num} of {player_suit}"
                   , "Result")

    if numbers.index(computer_num) > numbers.index(player_num):
        easygui.msgbox("The computer has the higher card\n"
                       "You Lose", "Computer Wins")

    elif numbers.index(computer_num) == numbers.index(player_num):
        easygui.msgbox("The computer has the same card as you,\n"
                       "You Tie", "Tie")

    else:
        easygui.msgbox("The computer has a lower card than you,\n"
                       "You Win!", "Player Win")

    play = easygui.buttonbox("Would you like to play?", "Play Again",
                         choices= ["Yes","No"])

easygui.msgbox("Goodbye")












