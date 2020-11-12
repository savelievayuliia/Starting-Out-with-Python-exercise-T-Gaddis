file = open("numbers.txt", "r")
summa = 0
for number in file:
    value = int(number)
    summa += value
file.close()

print("Sum of numbers in file is ", summa)
