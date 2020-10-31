years = int(input("Enter Q years we're going to calculate rainfall thickness for: "))
months = 2 * years
q_total_rainfall = 0.0
for y in range (1,years + 1):
    for x in range (1,months + 1,1):
        q_rainfall_month = float(input("Enter Q rainfall thickness in mm: "))
        q_total_rainfall += q_rainfall_month
    q_avg_rainfall = q_total_rainfall / months
    q_avg_rainfall_year = q_avg_rainfall * 12
    print(y,"\t",q_avg_rainfall_year)
    print("Total q of month: ", months)
    print("Total Q of rainfalls: ", q_total_rainfall)