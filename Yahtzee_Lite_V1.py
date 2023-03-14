"""Sipmlified Yahtzee game"""

# Import easygui and random from file
import easygui, random

# count on number of rolls
count = 1
# numbers on dice
NUMS = ["1","2","3","4","5","6"]


# looping function to play again
while True:
    play = easygui.buttonbox("Do you want to play Yahtzee! Lite", "Play",
                             choices=["Yes", "No"])
    # if not playing
    if play == "No":
        easygui.msgbox("Goodbye", "Goodbye Screen")
        break


    while count != 4:
        # list of rolls
        roll = []

        # Roll all five dice
        for die in range(0,5):
            dice = random.choice(NUMS)
            roll.append(dice)

        count += 1
        roll.sort()



        for item in roll:
            show_roll = f",  ".join(roll)

        choice = easygui.buttonbox(f"You rolled {show_roll}",f"Roll {count-1}",
                          choices= ["Roll Again", "Stick"])

        if choice == "Stick":
            counter = 0
            for option in roll:
                repeats = roll.count(option)
                if repeats > counter:
                    counter=repeats

            if counter == 5:
                easygui.msgbox("Yahtzee!", "Score")
                break
            elif counter == 4:
                easygui.msgbox("Four of a kind!", "Score")
                break
            elif counter == 3:
                easygui.msgbox("Three of a kind!", "Score")
                break
            elif counter == 2:
                easygui.msgbox("No matches made, better luck next time",
                               "Score")
                break
            elif counter == 0:
                easygui.msgbox("No matches made, better luck next time",
                               "Score")
                break
    easygui.msgbox("Good Game!", "Game End")
    count = 1





