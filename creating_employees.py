from ua.univer.lesson.lesson06.employee.employee_class import Employee

Sam = Employee("Sam", "0001", "HR", "manager")
Ben = Employee("Ben", "0002", "Research", "specialist")
Chris = Employee("Chris", "0003", "Production", "developer")
Ann = Employee("Ann", "0004", "Marketing", "marketer")

print(Sam.get_all_data())
print(Ben.get_all_data())
print(Chris.get_all_data())
print(Ann.get_all_data())
