import easygui

nz_word = easygui.enterbox("Please enter NZ word", "Word tp check")
letters = list(nz_word)
letters.remove("u")
easygui.msgbox(f"The American spelling of {nz_word} is {''.join(letters)}",
               "Result")
