MONTHS = 12
months_rains = []
for i in range(1, MONTHS + 1):
    print("Month # ", i)
    q_rains = float(input("Enter Q of rains during this month "))
    months_rains.append(q_rains)
    i += 1
total_rains = sum(months_rains)
average_rains = total_rains / MONTHS
max_rains = max(months_rains)
max_month = months_rains.index(max_rains)
min_rains = min(months_rains)
min_month = months_rains.index(min_rains)
print("Total Q of rains: ", total_rains)
print("Average Q of rains per month were: ", average_rains)
print("Max Q of rains were during: ", max_month + 1, "month")
print("Min Q of rains were during: ", min_month + 1, "month")
