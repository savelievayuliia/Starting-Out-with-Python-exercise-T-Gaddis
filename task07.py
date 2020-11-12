import random

file = open("random_numbers.txt", "w")
q_numbers = int(input("Enter Q of random number you'd like to get: "))

START_POINT = 1
END_POINT = 500

for i in range(1, q_numbers + 1):
    random_number = random.randint(START_POINT, END_POINT)
    file.write(str(random_number) + "\n")
    i += 1
file.close()
