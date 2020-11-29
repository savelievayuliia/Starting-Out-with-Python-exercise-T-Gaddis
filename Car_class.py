class Car:
    def __init__(self, year, manufacturer):
        self.__year_model = year
        self.__make = manufacturer
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        return self.__speed

    def stop(self):
        self.__speed -= 5
        return self.__speed

    def show(self):
        #return self.__year_model , self.__make , self.__speed
        print("Year: ", self.__year_model,"\n""Manufacturer: ", self.__make ,"\n""Speed: ", self.__speed)

    def get_speed(self):
        return self.__speed
