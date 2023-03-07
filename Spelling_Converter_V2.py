import easygui

# Ask the user to play
play = easygui.buttonbox("Would you like to play?", "Welcome",
                         choices= ["Yes","No"])
# loop to continue playing
while play == "Yes":

    # enter NZ word
    nz_word = easygui.enterbox("Please enter NZ word", "Word to check")

    # Check if word contains ise
    if "ise" in nz_word:
        us_word = nz_word.replace("ise", "ize")
        easygui.msgbox(f"The American spelling of {nz_word} is {us_word}",
                   "Result")

    # Check if word contains yse
    elif "yse" in nz_word:
        us_word = nz_word.replace("yse", "yze")
        easygui.msgbox(f"The American spelling of {nz_word} is {us_word}",
                   "Result")

    # Check if word contains our
    elif "our" in nz_word:
        us_word = nz_word.replace("our", "or")
        easygui.msgbox(f"The American spelling of {nz_word} is {us_word}",
                   "Result")

    # show if word is the same spelling
    else:
        easygui.msgbox("The spelling is the same in the USA and NZ", "Spelling"
                                                                     "Same")

    # ask user to play again
    play = easygui.buttonbox("Would you like to play again?", "Play again",
                         choices= ["Yes","No"])

# Tell user goodbye
easygui.msgbox("Goodbye", "Goodbye")
