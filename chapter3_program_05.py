mass = float(input("Введите массу обьекта: "))
COEFF = 9.8
weight = mass * COEFF
if weight > 500:
    print("Тело слишком тяжелое")
elif weight < 100:
        print("Тело слишком легкое")


