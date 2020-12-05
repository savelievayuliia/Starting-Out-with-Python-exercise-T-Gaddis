class Person:
    def __init__(self, name, address, telephone):
        self.__telephone = telephone
        self.__address = address
        self.__name = name

    def set_telephone(self, telephone):
        self.__telephone = telephone

    def set_address(self, address):
        self.__address = address

    def set_name(self, name):
        self.__name = name

    def get_telephone(self):
        return self.__telephone

    def get_address(self):
        return self.__address

    def get_name(self):
        return self.__name


class Customer(Person):
    def __init__(self, name, address, telephone, ID, yes_no_in_database):
        Person.__init__(self, name, address, telephone)
        self.yes_no_in_database = yes_no_in_database
        self.__ID = ID

    def set_ID(self, ID):
        self.__ID = ID

    def get_ID(self):
        return self.__ID

    def boolean(self, yes_no_in_database):
        yes_no_in_database = "yes"
