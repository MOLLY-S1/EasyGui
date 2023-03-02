
import easygui
import random

                   # name = easygui.enterbox("Hi! What's your name? ", "Name")

                   # age = easygui.integerbox("What's your age? ", "Age") #dont need interger checker

                   # button = easygui.buttonbox("Do you want continue?","Game Continue",
                                               #choices=["Yes", "No", "Maybe"])
                    #easygui.msgbox("Hi! Welcome to EasyGui", "Welcome")

# for i in range(100):
#     number = random.radint(0,5)
# words = ["Molly", "Jireh","Kgee", "Cat"]

word = "Absolute"
for i in range(5):
    letter= random.choice(word)
    easygui.msgbox(letter, f"letter {i+1} chosen")



