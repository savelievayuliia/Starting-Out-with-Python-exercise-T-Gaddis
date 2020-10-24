q_girls = int(input("Введите количество девочек: "))
q_boys = int(input("Введите количество мальчиков: "))
q_total = q_boys + q_girls
percent_girls = q_girls / q_total
percent_boys = q_boys / q_total
print("Процент девочек составляет",format(percent_girls,".1%"))
print("Процент мальчиков составляет",format(percent_boys,".1%"))