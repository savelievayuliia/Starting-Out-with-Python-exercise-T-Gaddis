myfile = open("numbers.txt", "r")
for i in myfile:
    number = int(i)
    print(number)
