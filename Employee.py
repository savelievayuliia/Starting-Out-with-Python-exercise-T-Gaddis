class Employee:
    def __init__(self, name, ID):
        self.__name = name
        self.__ID = ID

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_ID(self, ID):
        self.__ID = ID

    def get_ID(self):
        return self.__ID




class ProductionWorker(Employee):
    def __init__(self, name, ID, session_number, wage_ratio):
        Employee.__init__(self, name, ID)
        self.__session_number = session_number
        self.__wage_ratio = wage_ratio

    def set_session_number(self, session_number):
        self.__session_number = session_number

    def set_wage_ratio(self, wage_ratio):
        self.__wage_ratio = wage_ratio

    def get_session_number(self):
        return self.__session_number

    def get_wage_ratio(self):
        return self.__wage_ratio

class ShiftSupervisor(Employee):
    def __init__(self, name, ID, yearly_salary, year_premia):
        Employee.__init__(self, name, ID)
        self.__year_premia = year_premia
        self.__yearly_salary = yearly_salary

    def set_year_premia(self, year_premia):
        self.__year_premia = year_premia

    def set_yearly_salary(self, yearly_salary):
        self.__yearly_salary = yearly_salary

    def get_year_premia(self):
        return self.__year_premia

    def get_yearly_salary(self):
        return self.__yearly_salary


