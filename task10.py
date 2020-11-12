def getting_players_scores():
    file = open("golf.txt", "a")
    q_players = int(input("Enter Q players you want to add scores for "))
    try:
        for i in range(1, q_players + 1):
            player_name = str(input("Enter name of player "))
            player_score = float(input("Enter score of player "))
            file.write(str(player_name) + "\t")
            file.write(str(player_score) + "\t")
            file.write("\n")
            i += 1
    except:
        print("An error has occured")
    file.close()


def reading_players_scores():
    file = open("golf.txt", "r")
    for name in file:
        value1 = str(name)
        print(value1, end="")
    file.close()


reading_players_scores()
