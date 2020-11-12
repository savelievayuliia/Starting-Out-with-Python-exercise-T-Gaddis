file = open("random_numbers.txt", "r")
for number in file:
    amount = int(number)
    print(amount)
file.close()
