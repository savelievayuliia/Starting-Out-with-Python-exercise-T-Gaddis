def credit_spendings():
    credit = float(input("Enter costs for paying car's loan: "))
    return credit


def insurance_spendings():
    insurance = float(input("Enter costs for paying car's insurance: "))
    return insurance

def gas_spendings():
    gas = float(input("Enter costs for gas: "))
    return gas

def oil_spendings():
    oil = float(input("Enter costs for oil: "))
    return oil

def tiers_spendings():
    tiers = float(input("Enter costs for paying car's tiers: "))
    return tiers

def inspection_spendings():
    inspection = float(input("Enter costs for paying car's inspection: "))
    return inspection

def total_spendings():
    credit = credit_spendings()
    insurance = insurance_spendings()
    gas = gas_spendings()
    oil = oil_spendings()
    tires = tiers_spendings()
    inspection = inspection_spendings()
    total_car_costs = credit + insurance + gas + oil + tires + inspection
    print("Total costs for using your car amounted: $",format(total_car_costs,",.2f"))

total_spendings()