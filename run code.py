import random
import easygui as eg


def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]


def count_dice(dice_list):
    count_dict = {}
    for dice in dice_list:
        count_dict[dice] = count_dict.get(dice, 0) + 1
    return count_dict


def check_win(dice_list):
    counts = count_dice(dice_list)
    if 5 in counts.values():
        return "Yahtzee!", 50
    elif 4 in counts.values():
        return "Four of a kind!", 30
    elif 3 in counts.values():
        return "Three of a kind!", 10
    else:
        return "Better luck next time", 0


def play_game(player_name):
    eg.msgbox(f"Welcome {player_name} to Yahtzee Lite!")
    roll_count = 0
    dice_list = roll_dice()
    while roll_count < 3:
        msg = f"{player_name}, you rolled: {sorted(dice_list)}\nDo you want to roll again?"
        choice = eg.buttonbox(msg, choices=["Roll", "Stick"])
        if choice == "Roll":
            dice_list = roll_dice()
            roll_count += 1
        else:
            result, score = check_win(dice_list)
            eg.msgbox(f"{player_name}, you scored {score} points for {result}")
            return score
    result, score = check_win(dice_list)
    eg.msgbox(f"{player_name}, you scored {score} points for {result}")
    return score


def main():
    eg.msgbox("Welcome to Yahtzee Lite!")
    play_again = True
    while play_again:
        score1 = play_game("Player 1")
        score2 = play_game("Player 2")
        if score1 > score2:
            winner = "Player 1"
        elif score2 > score1:
            winner = "Player 2"
        else:
            winner = "It's a tie"
        choice = eg.buttonbox(f"{winner} won the game!\nDo you want to play again?", choices=["Yes", "No"])
        if choice == "No":
            play_again = False
    eg.msgbox("Thanks for playing Yahtzee Lite!")


if __name__ == "__main__":
    main()


from easygui import *
import random


def roll_dice():
    dice = []
    for num in range(5):
        dice.append(random.randint(1, 6))
    return dice


def stick(dice):
    for num in range(1, 7):
        if dice.count(num) == 3:
            return 10, "Three of a Kind"
        elif dice.count(num) == 4:
            return 30, "Four of a Kind"
        elif dice.count(num) == 5:
            return 50, "YAHTZEE!"
    return 0, "Better luck next time"


def play_turn(player):
    i = 1
    msgbox(f"{player['name']}, ready to roll?")
    while i <= 3:
        dice = roll_dice()
        choice = buttonbox(
            f"{player['name']}'s dice roll {i}\n\n"
            f"{player['name']} rolled: {dice}",
            "Random roll",
            choices=["Roll Again", "Stick"]
        )
        if choice == "Roll Again":
            i += 1
        elif choice == "Stick":
            points, msg = stick(dice)
            msgbox(
                f"{dice}\n\n"
                f"{msg}\n\n"
                f"{player['name']}'s points: {points}",
                "Result"
            )
            return points
    msgbox(
        f"{player['name']} ran out of rolls!\n\n"
        f"You score 0. Better luck next time",
        "Result"
    )
    return 0


def play_round(p1, p2):
    # players play their turns
    p1["points"] = play_turn(p1)
    p2["points"] = play_turn(p2)

    # figure out winner
    if p1["points"] > p2["points"]:
        winner, loser = p1, p2
    elif p1["points"] == p2["points"]:
        winner = "draw"
    else:
        winner, loser = p2, p1

    # display accordingly
    if winner == "draw":
        if ynbox(f"This was a draw!\n"
                 f"Both {p1['name']} and {p2['name']} scored "
                 f"{p1['points']}\n\n"
                 f"Do you want to play another round?",
                 "Round result"):
            return play_round(p1, p2)
    else:
        if ynbox(f"The winner is {winner['name']} with a score of "
                 f"{winner['points']}!\n\n"
                 f"{loser['name']} only scored {loser['points']}\n\n"
                 f"Would you like to play another round?",
                 "Round result"):
            return play_round(p1, p2)
    return msgbox("Goodbye", "See ya!")




# get player names
p1, p2 = {}, {}
p1["name"] = enterbox("Enter the name of player 1:", "Player 1").capitalize()
p2["name"] = enterbox("Enter the name of player 2:", "Player 2").capitalize()


play_round(p1, p2)
