import random

START = 0
END = 9
TOTAL_NUMBERS = 7
lottery = []
i = 1
for i in range(TOTAL_NUMBERS):
    random_number = random.randint(START, END)
    lottery.append(random_number)
    i += 1
print(lottery)
