"""Sipmlified Yahtzee game"""

# Import easygui and random from file
import easygui, random


def dice():
     # numbers on dice
    NUMS = ["1","2","3","4","5","6"]
    roll = []

    # Roll all five dice
    for die in range(0,5):
        dice = random.choice(NUMS)
        roll.append(dice)

    # add 1 to the round counter and sort the roll
    roll.sort()


    # Number formatting
    for item in roll:
        show_roll = f",  ".join(roll)

    return roll


def score_calc(roll):
    counter = 0
    for option in roll:
        repeats = roll.count(option)
        if repeats > counter:
            counter=repeats

            # Give corresponding score
            if counter == 5:
                return "Yahtzee!", 50

            elif counter == 4:
                return "Four of a kind!", 30


            elif counter == 3:
                return "Three of a kind!", 10

            elif counter <= 2:
                return "No matches made, better luck next time", 0


def turn():
    count = 1
    while count != 4:
        roll = dice()

        # Number formatting
        for item in roll:
            show_roll = f",  ".join(roll)

        # Print roll and give option to play again or stick
        choice = easygui.buttonbox(f"You rolled {show_roll}",f"Roll {count+1}",
                          choices= ["Roll Again", "Stick"])

        # Loop for if choice is stick
        if choice == "Stick":
            result = score_calc(roll)
            return result

        else:
            dice()
            count += 1


        # Reset count
    count = 1


play = easygui.buttonbox("Do you want to play?", "Play again",
                      choices=["Yes", "No"])
while play == "Yes":
    p1_name = easygui.enterbox("Enter player 1 name:", "Name 1")
    player1 = turn()
    p2_name = easygui.enterbox("Enter player 2 name:", "Name 2")
    player2 = turn()

    if player1 > player2:
        easygui.msgbox(f"The winner is {p1_name}", f"Winner {p1_name}")
    elif player1 < player2:
        easygui.msgbox(f"The winner is {p2_name}", f"Winner {p2_name}")
    else:
        easygui.msgbox(f"It is a tie between {p2_name} and {p1_name}", "Tie")

    play = easygui.buttonbox("Do you want to play again?", "Play again",
                      choices=["Yes", "No"])

easygui.msgbox("Goodbye","Goodbye")

