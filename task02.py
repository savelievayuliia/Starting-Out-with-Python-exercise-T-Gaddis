myfile_name = str(input("Enter the name of a file"))
file = open(myfile_name, "r")


def sum_lines():
    sum_lines = 0
    for lines in file:
        sum_lines += 1
    return sum_lines


if sum_lines() > 5:
    for i in range(0, 5):
        file = open(myfile_name, "r")
        data = file.readlines()[i]
        data = data.rstrip('\n')
        print(data)
        i += 1
else:
    file = open(myfile_name, "r")
    for i in file:
        print(i,end="")

file.close()
