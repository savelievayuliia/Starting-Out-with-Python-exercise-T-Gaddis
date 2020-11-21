def getting_list_of_capitals():
    import csv

    with open("capitals.csv", newline='') as capitals_list:
        capitals_dictionary = csv.reader(capitals_list, delimiter=";")
        capt_dict = {}
        for row in capitals_dictionary:
            capt_dict[row[0]] = row[1]
        return capt_dict


capitals = getting_list_of_capitals()
CORRECT = 0
INCORRECT = 0
again = "yes"
while again == "yes":
    state, capital = capitals.popitem()
    print("Random state name is: ", state)
    get_capital = input("Enter capital ")
    if get_capital == capital:
        print("Correct!")
        CORRECT += 1
        again = input("If you want to continue, type yes: ")
    else:
        print("Its incorrect")
        INCORRECT += 1
        again = input("If you want to continue, type yes: ")
print("You've finished the game")
print("Correct answers: ", CORRECT)
print("Incorrect answers: ", INCORRECT)
