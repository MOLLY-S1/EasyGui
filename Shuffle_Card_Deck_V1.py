import easygui,random

numbers = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
suits = ["Clubs","Diamonds","Hearts","Spades"]

deck = []
draw = []
for suit in suits:
    for card in numbers:
        deck.append([card, suit])

while True:
    play = easygui.buttonbox("Do you want to play", "Play",
                             choices=["Yes", "No"])
    if play == "No":
        break

    random.shuffle(deck)
    for card in deck [0:7]:
        draw.append(f"Card {deck.index(card)+1} {card[0]} of {card[1]}")
    for item in draw:
        show_cards = f"\n*   ".join(draw)




    easygui.msgbox(f"You have drawn\n\n*   {show_cards}",
                              "Random Draw")


easygui.msgbox("Goodbye", "Goodbye Screen")
