import csv


def creating_dictionary_from_file(user_file):
    with open(user_file) as file:
        dictionary = {}
        set_of_names = set()
        list = []
        count = 0
        working_file = csv.reader(file)
        for item in working_file:
            for word in item:
                list.append(word)
                set_of_names.add(word)
        #print(set_of_names)
        for name in set_of_names:
            dictionary[name] = list.count(name)
        print(dictionary)


creating_dictionary_from_file("names.csv")
