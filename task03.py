date_input = str(input("Enter dat in dd/mm/yyyy "))


def printing_date(date):
    date_splited = date.split("/")
    if date_splited[1] == "01":
        correct_date = date_splited[0] + " " + "january" + " " + date_splited[2]
    if date_splited[1] == "02":
        correct_date = date_splited[0] + " " + "feb" + " " + date_splited[2]
    if date_splited[1] == "03":
        correct_date = date_splited[0] + " " + "march" + " " + date_splited[2]
    if date_splited[1] == "04":
        correct_date = date_splited[0] + " " + "april" + " " + date_splited[2]
    if date_splited[1] == "05":
        correct_date = date_splited[0] + " " + "may" + " " + date_splited[2]
    if date_splited[1] == "06":
        correct_date = date_splited[0] + " " + "june" + " " + date_splited[2]
    if date_splited[1] == "07":
        correct_date = date_splited[0] + " " + "july" + " " + date_splited[2]
    if date_splited[1] == "08":
        correct_date = date_splited[0] + " " + "august" + " " + date_splited[2]
    if date_splited[1] == "09":
        correct_date = date_splited[0] + " " + "sept" + " " + date_splited[2]
    if date_splited[1] == "10":
        correct_date = date_splited[0] + " " + "oct" + " " + date_splited[2]
    if date_splited[1] == "11":
        correct_date = date_splited[0] + " " + "nov" + " " + date_splited[2]
    if date_splited[1] == "12":
        correct_date = date_splited[0] + " " + "dec" + " " + date_splited[2]
    print(correct_date)


printing_date(date_input)
