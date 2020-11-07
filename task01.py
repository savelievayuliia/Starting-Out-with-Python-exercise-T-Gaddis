sales = []
DAYS = 7
i = 1
for i in range(DAYS):
    print("Day ", i + 1)
    sales_day = float(input("Enter sales value for the day: "))
    sales.append(sales_day)
    i += 1
total_sales = sum(sales)
print("Total sales during the week amounted: ", format(total_sales, ",.2f"))
