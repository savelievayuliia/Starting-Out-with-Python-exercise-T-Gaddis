FED_TAX = 0.05
MUNICIPAL_TAX = 0.025
Q_sales = float(input("Enter totals sales in $: "))


def fed_tax_calculation():
    fed_tax = Q_sales * FED_TAX
    return fed_tax


def municipal_tax_calculation():
    municipal_tax = Q_sales * MUNICIPAL_TAX
    return municipal_tax


def total_taxes():
    fed_tax = fed_tax_calculation()
    municipal_tax = municipal_tax_calculation()
    total_tax = fed_tax + municipal_tax
    print("Federal taxes amounted: $", format(fed_tax, ",.2f"))
    print("Municipal taxes amounted: $", format(municipal_tax, ",.2f"))
    print("Total taxes amounted: $", format(total_tax, ",.2f"))


total_taxes()
