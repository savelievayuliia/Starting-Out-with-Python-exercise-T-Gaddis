from chapter_11.Employee import ProductionWorker, ShiftSupervisor

name = str(input("Enter the name of the worker: "))
identification = int(input("Enter the ID of the worker: "))
session_number = int(
    input("Enter 1 if the worker has worked the first shift, or 2 if he or she has worked the second shift : "))
wage = float(input("Enter the worker's wage ratio - USD per hour: "))
name1 = str(input("Enter the name of the supervisor: "))
identification1 = int(input("Enter the ID of the supervisor: "))
yearly_salary = float(input("Enter the supervisor's wage ratio - USD per year: "))
year_premia = float(input("Enter the supervisor's premia per year: "))

worker = ProductionWorker(name, identification, session_number, wage)
supervisor = ShiftSupervisor(name1, identification1, yearly_salary, year_premia)

print(worker.get_name())
print(worker.get_ID())
print(worker.get_session_number())
print(worker.get_wage_ratio())

print(supervisor.get_name())
print(supervisor.get_ID())
print(supervisor.get_yearly_salary())
print(supervisor.get_year_premia())
