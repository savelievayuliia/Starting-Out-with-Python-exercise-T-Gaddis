from chapter_11_task03.Person import Customer


def work_with_customer():
    name = str(input("Enter your name: "))
    identification = int(input("Enter your ID: "))
    address = str(input("Enter your address: "))
    phone = int(input("Enter your phone number: "))
    yes_no = str(input("Do you want to be added to our database? Yes / no: : "))
    customer = Customer(identification, address, name, phone, yes_no)
    print(customer.boolean(yes_no))


work_with_customer()
