class Procedure:
    def __init__(self, procedure, date, doctor, price):
        self.__procedure = procedure
        self.__date = date
        self.__doctor = doctor
        self.__price = price

    def set_procedure(self, procedure):
        self.__procedure = procedure

    def set_date(self, date):
        self.__date = date

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def set_price(self, price):
        self.__price = price

    # get
    def get_all(self):
        return self.__procedure, self.__date, self.__doctor, self.__price

    def get_procedure(self):
        return self.__procedure

    def get_date(self):
        return self.__date

    def get_doctor(self):
        return self.__doctor

    def get_price(self):
        return self.__price
