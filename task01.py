def course_dictionary():
    auditory1 = 3004
    auditory2 = 4501
    auditory3 = 6755
    auditory4 = 1244
    auditory5 = 1411
    lector1 = "Heins"
    lector2 = "Alvarado"
    lector3 = "Rich"
    lector4 = "Berk"
    lector5 = "Lee"
    time1 = "8 a.m"
    time2 = "9 a.m"
    time3 = "10 a.m"
    time4 = "11 a.m"
    time5 = "1 p.m"
    course_dictionary = {}
    course_dictionary["CS101"] = [auditory1] + [lector1] + [time1]
    course_dictionary["CS102"] = [auditory2] + [lector2] + [time2]
    course_dictionary["CS103"] = [auditory3] + [lector3] + [time3]
    course_dictionary["NT110"] = [auditory4] + [lector4] + [time4]
    course_dictionary["CM241"] = [auditory5] + [lector5] + [time5]

    return course_dictionary


# print(course_dictionary())
course_number = input("Enter course number: ")
course = course_dictionary()
item = course.get(course_number, "No such course")
print("Auditory number: ", item[0], "\n", "Lector: ", item[1], "\n", "Time: ", item[2])
