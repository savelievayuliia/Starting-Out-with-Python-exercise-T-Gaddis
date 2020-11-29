from ua.univer.lesson.lesson06.patient.Patient import Patient
from ua.univer.lesson.lesson06.patient.Procedure import Procedure

Tonya = Patient("Tonya", "Vladmirovna", "Bebko", "Pushkina 1", "Kyiv", "Pechersk", "02078", "34543646",
                "Holovko Inna Valeriivna",
                "54787686876")
Procedure1 = Procedure("Врачебный осмотр", "28 ноября 2020", "Ирвин", "250.00")
Procedure2 = Procedure("Рентгеноскопия", "28 ноября 2020", "Джемисон", "500.00")
Procedure3 = Procedure("Анализ крови", "28 ноября 2020", "Смит", "200.00")


def total_costs():
    price1 = float(Procedure1.get_price())
    price2 = float(Procedure2.get_price())
    price3 = float(Procedure3.get_price())
    costs = price1 + price2 + price3
    print("Общая стоимость процедур ", costs)


print(Tonya.get_all())
print(Procedure1.get_all())
print(Procedure2.get_all())
print(Procedure3.get_all())
total_costs()
