month = int(input("Введите месяц в числовой форме: "))
day = int(input("Введите день: "))
year = int(input("Введите год в двузначном формате: "))
day_month = day * month
if day_month == year:
    print(" Введенная дата является волшебной")
else:
    print("Введенная дата не является волшебной")