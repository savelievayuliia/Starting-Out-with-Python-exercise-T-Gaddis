TAX = 0.07
price_1 = float(input("Введите цену товара 1: "))
price_2 = float(input("Введите цену товара 2: "))
price_3 = float(input("Введите цену товара 3: "))
price_4 = float(input("Введите цену товара 4: "))
price_5 = float(input("Введите цену товара 5: "))
total_price = price_1 + price_2 + price_3 + price_4 + price_5
tax_value = TAX * total_price
total_value = total_price + tax_value
print("Сумма покупки стоставила: ", format(total_price, ",.2f"))
print("Сумма налога стоставила: ", format(tax_value, ",.2f"))
print("Сумма вместе с налогом стоставила: ", format(total_value, ",.2f"))
