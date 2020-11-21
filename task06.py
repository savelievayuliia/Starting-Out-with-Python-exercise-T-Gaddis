import csv


def getting_set_from_file(user_file):
    with open(user_file) as file:
        words = csv.reader(file)
        words_set = set()
        for item in words:
            for word in item:
                words_set.add(word)
        return words_set


def compare_two_files_sets(file_1, file_2):
    set_for_file_1 = getting_set_from_file(file_1)
    set_for_file_2 = getting_set_from_file(file_2)
    # 1
    print("We'll show you all unique words in both files: ")
    print(set_for_file_1)
    print(set_for_file_2)
    # 2
    print("We'll show you words that are in both files: ")
    print(set_for_file_1.intersection(set_for_file_2))
    # 3
    print("We'll show you words that are in 1st file, but not in the 2nd: ")
    print(set_for_file_1.difference(set_for_file_2))
    # 4
    print("We'll show you words that are in 2nd file, but not in the 1st: ")
    print(set_for_file_2.difference(set_for_file_1))
    # 5
    print("We'll show you words that are in the 1st or in 2nd file, but not in both: ")
    print(set_for_file_1.symmetric_difference(set_for_file_2))


compare_two_files_sets("names.csv", "names_v02.csv")
