from ua.univer.lesson.lesson06.employee.employee_class import Employee
import pickle

def creating_employees_dict():
    more = "yes"
    data = {}
    while more == "yes":
        name = input("Enter employee's name ")
        ID = input("Enter employee's ID ")
        department = input("Enter employee's department ")
        position = input("Enter employee's position ")
        employee = Employee(name, ID, department, position)
        data[ID] = name, department, position
        more = input("Have some more employees to add? Type 'yes' ")
    print(data)
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)


creating_employees_dict()
