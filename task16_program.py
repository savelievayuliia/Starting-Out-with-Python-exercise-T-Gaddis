first_score = "A"
second_score = "B"
third_score = "C"
fourth_score = "D"
fifth_score = "F"


def marks():
    mark1 = float(input("Enter your 1st mark: "))
    mark2 = float(input("Enter your 2nd mark: "))
    mark3 = float(input("Enter your 3d mark: "))
    mark4 = float(input("Enter your 4th mark: "))
    mark5 = float(input("Enter your 5th mark: "))
    return mark1, mark2, mark3, mark4, mark5


mark1, mark2, mark3, mark4, mark5 = marks()


def calc_average():
    calc_average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
    return calc_average


def marks_score():
        if mark1 >= 90:
            mark1_score = str(first_score)
        elif 80 <= mark1 < 90:
            mark1_score = str(second_score)
        elif 70 <= mark1 < 79:
            mark1_score = str(third_score)
        elif 60 <= mark1 < 69:
            mark1_score = str(fourth_score)
        elif mark1 < 60:
            mark1_score = str(fifth_score)
            #mark2
        if mark1 >= 90:
            mark1_score = str(first_score)
        elif 80 <= mark1 < 90:
            mark1_score = str(second_score)
        elif 70 <= mark1 < 79:
            mark1_score = str(third_score)
        elif 60 <= mark1 < 69:
            mark1_score = str(fourth_score)
        elif mark1 < 60:
            mark1_score = str(fifth_score)
            #mark3
        if mark1 >= 90:
            mark1_score = str(first_score)
        elif 80 <= mark1 < 90:
            mark1_score = str(second_score)
        elif 70 <= mark1 < 79:
            mark1_score = str(third_score)
        elif 60 <= mark1 < 69:
            mark1_score = str(fourth_score)
        elif mark1 < 60:
            mark1_score = str(fifth_score)
        #mark4
        if mark1 >= 90:
            mark1_score = str(first_score)
        elif 80 <= mark1 < 90:
            mark1_score = str(second_score)
        elif 70 <= mark1 < 79:
            mark1_score = str(third_score)
        elif 60 <= mark1 < 69:
            mark1_score = str(fourth_score)
        elif mark1 < 60:
            mark1_score = str(fifth_score)
        #mark5
        if mark1 >= 90:
            mark1_score = str(first_score)
        elif 80 <= mark1 < 90:
            mark1_score = str(second_score)
        elif 70 <= mark1 < 79:
            mark1_score = str(third_score)
        elif 60 <= mark1 < 69:
            mark1_score = str(fourth_score)
        elif mark1 < 60:
            mark1_score = str(fifth_score)
            #return

        return mark1_score

average_mark = calc_average()
print("Your average mark is: ", average_mark)
mark1_score = marks_score()
mark2_score = marks_score()
mark3_score = marks_score()
mark4_score = marks_score()
mark5_score = marks_score()

print("Marks scores")
print(mark1, mark1_score)