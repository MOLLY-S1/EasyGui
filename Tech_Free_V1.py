import easygui

GOAL = 3

days_used = easygui.enterbox("Enter the days you used technology, "
                             "seperated by a space", "Days Tech was Used"). \
    split()
days = len(days_used)

free = 7 - days

if free >= GOAL:
    easygui.msgbox(f"Well Done!\n"
                   f"You acheived your goal of {GOAL} days with {free} "
                   f"days free of technology", "Goal Achieved")

else:
    easygui.msgbox(f"Oh No!\n"
                   f"You did not acheive your goal of {GOAL} days with only"
                   f" {free} days without technology", "Goal Not Achieved")
