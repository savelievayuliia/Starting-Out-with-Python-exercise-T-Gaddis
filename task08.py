def girls_names_list():
    girls_names = []
    infile = open('girls.txt', 'r')
    girls_names = infile.read().splitlines()
    infile.close()
    return girls_names


def boys_names_list():
    boys_names = []
    infile = open('boys.txt', 'r')
    boys_names = infile.read().splitlines()
    infile.close()
    return boys_names


def checking_name_in_the_list():
    names_from_the_user = []
    want_more_answer = "yes"
    while want_more_answer == "yes":
        name_to_check = str(input("Enter the name you want to check "))
        names_from_the_user.append(name_to_check)
        want_more_answer = str(input("Type yes if you'd like to enter more names "))
    for item in names_from_the_user:
        if item in girls_names_list():
            print("Name ", item, " is in the list")
        elif item in boys_names_list():
            print("Name ", item, " is in the list")
        else:
            print("The name", item, "is not in the list")


checking_name_in_the_list()
