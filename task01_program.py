Q_DAYS = 5
Q_errors_starting = 0.0
errors = Q_errors_starting
for days in range(Q_DAYS):
    q = int(input("Print count of errors during the day: "))
    errors = errors + q
print("Total number of errors per week: ", int(errors))
