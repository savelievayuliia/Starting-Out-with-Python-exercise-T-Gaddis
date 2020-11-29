from ua.univer.lesson.lesson06.retail_item.RetailItem_class import RetailItem
from ua.univer.lesson.lesson06.cashregister.CashRegister import CashRegister

apple = RetailItem("apple", 0, 1)
snickers = RetailItem("snickers", 0, 2)
cola = RetailItem("cola", 0, 3)

shop_goods = [apple, snickers, cola]
customer_choice = []

kassa = CashRegister(customer_choice)

print("Welcome to our online store")
print("See the list of items below. Choose the item you'd like to purchase")
for item in shop_goods:
    print(item.get_descriprion())


more_goods = "yes"
while more_goods == "yes":
    item_input = input("Enter item name: ")
    how_many_input = input("Quantity: ")
    for item in shop_goods:
        if item.get_descriprion() == item_input:
            item.set_quantity(how_many_input)
            customer_choice.append(item)
            kassa.purchase_item(item)
    more_goods = input("If you want to continue shopping, type 'yes'. Otherwise you'll be moved to checkout: ")

kassa.show_items()
kassa.get_total()
