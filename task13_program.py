start_q_organisms = int(input("Enter current quantity of organisms: "))
avg_increase_per_day_percent = int(input("Enter the % of increase of quantity per day: "))
avg_increase_per_day = avg_increase_per_day_percent / 100
q_days_for_reporduction = int(input("Enter q days for reproduction: "))
start_date = 1
extra_for_day = 0.0
for x in range (start_date, q_days_for_reporduction + 1):
    total_for_day = int(start_q_organisms * ((1 + avg_increase_per_day / q_days_for_reporduction)**(x*q_days_for_reporduction)))
    print(x,"\t",total_for_day)