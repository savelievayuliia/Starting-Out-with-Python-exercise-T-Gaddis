CALORIES_BURNED_PER_MINUTE = 4.2
print("Minutes spent\tCalories burned")
for time in range (10,31,10):
    x = (time)
    calories_burned = x * CALORIES_BURNED_PER_MINUTE
    print(x,"\t",calories_burned)