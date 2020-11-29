class Patient:
    def __init__(self, name, middle_name, surname, address, city, region, index, phone, emergency_name,
                 emergency_contact):
        self.__name = name
        self.__middle_name = middle_name
        self.__surname = surname
        self.__address = address
        self.__city = city
        self.__region = region
        self.__index = index
        self.__phone = phone
        self.__emergency_name = emergency_name
        self.__emergency_contact = emergency_contact

    def set_name(self, name):
        self.__name = name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_surname(self, surname):
        self.__surname = surname

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_region(self, region):
        self.__region = region

    def set_index(self, index):
        self.__index = index

    def set_phone(self, phone):
        self.__phone = phone

    def set_emergency_name(self, emergency_name):
        self.__emergency_name = emergency_name

    def set_emergency_contact(self, emergency_contact):
        self.__emergency_contact = emergency_contact

    # get
    def get_all(self):
        return self.__name, self.__middle_name, self.__surname, self.__address, self.__city, self.__region, self.__index, self.__phone, self.__emergency_name, self.__emergency_contact

    def get_name(self):
        return self.__name

    def get_middle_name(self):
        return self.__middle_name

    def get_surname(self):
        return self.__surname

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_region(self):
        return self.__region

    def get_index(self):
        return self.__index

    def get_phone(self):
        return self.__phone

    def get_emergency_name(self):
        return self.__emergency_name

    def get_emergency_contact(self):
        return self.__emergency_contact
