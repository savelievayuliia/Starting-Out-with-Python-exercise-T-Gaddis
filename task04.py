file = open("names.txt", "r")


def sum_lines():
    sum_lines = 0
    for lines in file:
        sum_lines += 1
    return sum_lines


print("The file contains of ", sum_lines(), " names")
