distance = float(input("Введите пройденные километры: "))
gas_mileage = float(input("Введите расход бензина Вашей машины из расчета литров на 1 км: "))
gas_used = distance * gas_mileage
print("Вы потратили", format(gas_used, '.1f'), "литров бензина.")
