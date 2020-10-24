age = float(input("Введите возраст ребенка: "))
if age > 0 and age <= 1:
    print("младенец")
elif age > 1 and age <= 13:
    print("ребенок")
elif age > 13 and age <= 20:
    print("подросток")
elif age > 20:
    print("взрослый")
else:
    print("Данные введены не корректно")
