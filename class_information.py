class Information:

    def __init__(self, name, address, age, telephone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__telephone = telephone

    def get_name(self):
        return self.__name

    def update_name(self, new_name):
        self.__name = new_name

    def get_address(self):
        return self.__address

    def update_address(self, new_address):
        self.__address = new_address

    def get_age(self):
        return self.__age

    def update_age(self, new_age):
        self.__age = new_age

    def get_telephone(self):
        return self.__telephone

    def update_telephone(self, new_telephone):
        self.__telephone = new_telephone
