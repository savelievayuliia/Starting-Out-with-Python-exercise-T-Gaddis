def main():
    distance = float(input("Enter distance in km: "))
    calculation(distance)


def calculation(kilometers):
    koeff = 0.6214
    miles = kilometers * koeff
    print("Miles: ", format(miles, ".2f"))


main()
