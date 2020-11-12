myfile_name = str(input("Enter the name of a file"))
file = open(myfile_name, "r")


def sum_lines():
    sum_lines = 0
    for lines in file:
        sum_lines += 1
    return sum_lines


list = []
count = 1
for count in range(sum_lines()):
    for i in open(myfile_name, "r"):
        list.append(i)
    print(count+1, list[count])
    count += 1
