import easygui

fav_place = easygui.enterbox("Enter the names of 5 of your favourite places to visit"
                             ".\n" "Seperate each with a comma",
                             "Enter Favourite Places")

places = fav_place.split(",")

while len(places)> 5:
    easygui.msgbox(f"Sorry, but you can only enter 5 places, you entered "
                   f"{len(places)} ", "Error")
    fav_place = easygui.enterbox("Enter the names of 5 of your favourite places to visit"
                             ".\n" "Seperate each with a comma",
                             "Enter Favourite Places")
    places = fav_place.split(",")

while len(places)<5:
      easygui.msgbox(f"Sorry, but you need to enter 5 places, you entered "
                   f"{len(places)} ", "Error Also")
      fav_place = easygui.enterbox("Enter the names of 5 of your favourite places to visit"
                             ".\n" "Seperate each with a comma",
                             "Enter Favourite Places")
      places = fav_place.split(",")

easygui.msgbox(f"My Favourite Places:\n"
               f"- {places[0]}\n"
               f"- {places[1]}\n"
               f"- {places[2]}\n"
               f"- {places[3]}\n"
               f"- {places[4]}\n")



