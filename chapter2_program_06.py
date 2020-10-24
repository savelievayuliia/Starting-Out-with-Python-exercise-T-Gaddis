FEDERAL_SALES_TAX = 0.05
REGIONAL_SALES_TAX =  0.025
shopping_cart = float(input("Введите сумму покупки: "))
federal_tax_value = FEDERAL_SALES_TAX * shopping_cart
regional_tax_value = REGIONAL_SALES_TAX * shopping_cart
total_taxes_values = federal_tax_value + regional_tax_value
shopping_cart_taxes_value = shopping_cart + total_taxes_values
print("Сумма федерального налога",format(federal_tax_value,",.2f"))
print("Сумма регионального налога",format(regional_tax_value,",.2f"))
print("Сумма всех налогов",format(total_taxes_values,",.2f"))
print("Сумма покупки с учетом всех налогов",format(shopping_cart_taxes_value,",.2f"))
