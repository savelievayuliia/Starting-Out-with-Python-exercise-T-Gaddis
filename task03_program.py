sum_per_month = float(input("Enter the amount of money that you've intended for the month: "))
costs = 0.0
keep_going = "yes"
while keep_going == "yes":
    extra_cost = int(input("Enter the amount of a particular spending: "))
    costs += extra_cost
    keep_going = input("Did you have more spending this month? I yes, print yes: ")
print("Your total costs for this month were: $", format(costs,",.2f"))
net = sum_per_month - costs
if net > 0:
    print("You're having a surplus this month: $",net)
elif net == 0:
    print("You're current balance is equal to ",net)
elif net < 0:
    print("You're already having losses this month: $")

