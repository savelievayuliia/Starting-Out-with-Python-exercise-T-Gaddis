import csv


def getting_names_from_file(users_file):
    set_of_names = set()
    with open(users_file) as file:
        working_file = csv.reader(file)
        for item in working_file:
            for word in item:
                set_of_names.add(word)
        print(set_of_names)
        print(len(set_of_names))


getting_names_from_file("names.csv")
