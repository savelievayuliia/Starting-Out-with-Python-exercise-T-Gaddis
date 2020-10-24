MARGIN_RATE = 0.23
sales = float(input("Введите общий обьем продаж, в дол. США "))
profit = sales * MARGIN_RATE
print("Прибыль от продаж составила, дол. США: ", format(profit, ",.2f"))
