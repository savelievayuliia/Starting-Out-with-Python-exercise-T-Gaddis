BASE_COLOUR_1 = "красный"
BASE_COLOUR_2 = "синий"
BASE_COLOUR_3 = "желтый"

colour_1 = str(input("Введите один из основных цветов: "))
if colour_1 != BASE_COLOUR_1 and colour_1 != BASE_COLOUR_2 and colour_1 != BASE_COLOUR_3:
    print("Ошибка ввода цвета")

colour_2 = str(input("Введите еще один основной цвет: "))
if colour_2 != BASE_COLOUR_1 and colour_2 != BASE_COLOUR_2 and colour_2 != BASE_COLOUR_3:
    print("Ошибка ввода цвета")
    exit()

if colour_2 == BASE_COLOUR_1 or colour_2 == BASE_COLOUR_2 or colour_2 == BASE_COLOUR_3:
        if colour_1 == "красный" and colour_2 == "синий":
            print("фиолетовый")
        if colour_1 == "красный" and colour_2 == "желтый":
            print("оранжевый")
        if colour_1 == "синий" and colour_2 == "желтый":
            print("зеленый")
