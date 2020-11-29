from ua.univer.lesson.lesson06.car.Car_class import Car


def creating_car():
    year = input("Enter year of the car model ")
    manufacturer = input("Enter manufacturer of the car model ")
    car = Car(year, manufacturer)
    car.show()
    for x in range(5):
        car.accelerate()
    print("After 5x acceleration: ")
    car.show()
    for x in range(5):
        car.stop()
    print("After 5 breaks: ")
    car.show()


creating_car()
