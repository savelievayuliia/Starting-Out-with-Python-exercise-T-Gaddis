Q_numbers = 20
numbers_list = []
for i in range(Q_numbers):
    number = int(input("Enter integer number: "))
    numbers_list.append(number)
    i += 1
min_number = min(numbers_list)
max_number = max(numbers_list)
sum_numbers = sum(numbers_list)
average_numbers = sum_numbers / Q_numbers
print("Min number were: ", min_number)
print("Max number were: ", max_number)
print("Sum of numbers were: ", sum_numbers)
print("Average of numbers were: ", average_numbers)
