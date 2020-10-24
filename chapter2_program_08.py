TIPS = 0.18
SALES_TAX = 0.07
sales = float(input("Введите сумму счета: "))
sales_tax_value = SALES_TAX * sales
tips_value = TIPS * sales
net_food_costs = sales - sales_tax_value - tips_value
print("Сумма налога от продаж: ",format(sales_tax_value,",.2f"))
print("Сумма чаевых: ",format(tips_value,",.2f"))
print("Себестоимость еды: ",format(net_food_costs,",.2f"))



