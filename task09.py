file = open("numbers.txt", "r")
q_numbers = 0
summa = 0
try:
    for number in file:
        value = int(number)
        summa += value
        q_numbers += 1
    file.close()

    average_numbers = summa / q_numbers
    print("Sum of numbers in file is ", average_numbers)
except IOError:
    print("IOError has occured")
    print("Can't read data from file")
except ValueError:
    print("Value error")
