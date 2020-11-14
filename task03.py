number = int(input("Enter integer number "))

list_stars = []
for i in range(number+1):
    list_stars.append("*")


def integer_number_detection(n):
    if n > 0:
        print((n * list_stars[n]), end="\n")
        integer_number_detection(n - 1)


integer_number_detection(number)
