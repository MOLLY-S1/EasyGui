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

    
    while count <= 3:
        # list of rolls
        roll = []

        # Roll all five dice
        for die in range(0,5):
            dice = random.choice(NUMS)
            roll.append(dice)

        count += 1
        sort_roll = roll.sort()
        choice = easygui.buttonbox(f"You rolled {sort_roll}",f"Roll {count-1}",
                          choices= ["Roll Again", "Stick"])
        if choice == "Stick":



