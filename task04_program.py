time = int(input("Enter the quantity of hours the car has been driving? "))
speed = float(input("What was the car's speed? "))
print("Time\tDistance passed")
distance_passed = 0.0
time_spent = 1
for x in range(time_spent,time + 1, 1):
    distance = time * speed
    distance_passed += distance
    print(x, "\t", format(distance_passed, ".2f"), "km")
