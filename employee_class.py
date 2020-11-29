class Employee:
    def __init__(self, name, ID, department, position):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__position = position

    def get_all_data(self):
        return self.__name , self.__ID, self.__department, self.__position

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_department(self):
        return self.__department

    def get_position(self):
        return self.__position
