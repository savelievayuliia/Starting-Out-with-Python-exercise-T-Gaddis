import csv
import pickle


def getting_dictionary(users_file):
    with open(users_file) as file:
        emails_dictionary = {}
        data_file = csv.reader(file, delimiter=";")
        for item in data_file:
            emails_dictionary[item[0]] = item[1]
        return emails_dictionary


def finding_emails():
    key = input("Enter the name of person whose email you want to search for: ")
    email = EMAIL[key]
    print(key, " email is ", email)


def add_name_email():
    key = input("Enter the name of the person you'd like to add: ")
    value = input("Enter his or her email: ")
    EMAIL[key] = value
    return EMAIL


def change_email():
    key = input("Enter the name of a person whose email you'd like to change: ")
    value = input("Enter new email: ")
    EMAIL[key] = value
    print("Data was updated")
    return EMAIL


def delete_name_email():
    key = input("Enter the name of a person whose data you'd like to delete: ")
    name = EMAIL.pop(key, "No such name")
    print("Data ", name, " deleted")
    return EMAIL


def menu():
    # MENU
    print("Choose the option:")
    print("1. Find email")
    print("2. Add new name & email")
    print("3. Edit email")
    print("4. Delete name & email")
    actions = input("Enter number from the menu: ")
    if actions == "1":
        edits = finding_emails()
    elif actions == "2":
        edits = add_name_email()
    elif actions == "3":
        edits = change_email()
    elif actions == "4":
        edits = delete_name_email()


# def conserve_dictionary():
#   outputfile = open("conserved_dict","wb")
#  pickle.dump(dictionary,)


def work_with_user():
    again = "yes"
    while again == "yes":
        menu()
        again = input("Want to make more edits? Type yes: ")
    print("Thanks, your edits were saved and the dictionary was conserved")


print("Welcome to the database of names & emails")
users_file = input("Enter the name of csv file you want to work with: ")
EMAIL = getting_dictionary(users_file)
work_with_user()
