number = int(input("Print the number to calculate factorial for: "))
factorial_start = 1
for x in range(1, number + 1):
    factorial_start *= x
print("Factorial = ", factorial_start)
