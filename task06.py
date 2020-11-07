def createListNumbers():
    list_numbers = []
    for number in range(1,7):
        list_item = int(input("Enter num "+str(number)+": "))
        list_numbers.append(list_item)
    return list_numbers

def function1(x, y):
    for item in x:
        if item > y:
            print(item)

number = int(input("Enter integer number to compare the list with: "))
function1(createListNumbers(), number)
