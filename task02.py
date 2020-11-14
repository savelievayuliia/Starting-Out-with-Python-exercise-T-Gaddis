number1 = int(input("Enter integer number x "))
number2 = int(input("Enter integer number y "))

list_x = []


def function(x, y):
    if y > 0:
        list_x.append(x)
        function(x,y-1)
    summa_x = sum(list_x)
    return list_x , summa_x

print(function(number1, number2))