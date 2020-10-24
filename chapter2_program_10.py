sugar_cups_1_bun = 1.5 / 48
flower_cups_1_bun = 2.75 / 48
butter_cups_1_bun = 1 / 48
q_buns = int(input("Введите количество булочек, которые хотите испечь: "))
q_sugar_required = sugar_cups_1_bun * q_buns
q_flower_required = flower_cups_1_bun * q_buns
q_butter_required = butter_cups_1_bun * q_buns
print("Используйте",format(q_sugar_required,".2f"),"стаканов сахара")
print("Используйте",format(q_flower_required,".2f"),"стаканов муки")
print("Используйте",format(q_butter_required,".2f"),"стаканов масла")
