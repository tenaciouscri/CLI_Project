from data import warehouse1, warehouse2
import pprint
pp = pprint.PrettyPrinter(indent=4)

name = input("Hello! What is your username? ")

print(f"Welcome, {name}!")
print("What would you like to do?", 
      "1. List items by warehouse", 
      "2. Search an item and place an order", 
      "3. Quit", sep="\n")
print()

valid_input = False
while not valid_input:
    user_input = int(input("Please select your choice by entering its corresponding number: "))
    if user_input == 1:
        print("Here's the content of Warehouse 1:")
        pp.pprint(warehouse1)
        print()
        print("And here's the content of Warehouse 2:")
        pp.pprint(warehouse2)
        valid_input = True
    elif user_input == 2:
        user_item = input("What is the name of the item? ")
        count = warehouse1.count(user_item) + warehouse2.count(user_item)
        print(f"Amount available: {count}")
        if user_item in warehouse1 and warehouse2:
            print("Location: Both Warehouses")
        elif user_item in warehouse1:
            print("Location: Warehouse 1")
        elif user_item in warehouse2:
            print("Location: Warehouse 2")
        else:
            print("Not in stock")
        if warehouse1.count(user_item) > warehouse2.count(user_item):
            print(f"Maximum availability: {warehouse1.count(user_item)} in Warehouse 1")
        elif warehouse1.count(user_item) < warehouse2.count(user_item):
            print(f"Maximum availability: {warehouse2.count(user_item)} in Warehouse 2")
        else:
            pass
        print()
        if count >= 1:
            order_yn = input("Would you like to place an order for this item? (Y/N) ")
            valid_amount = False
            if order_yn == "Y":
                while not valid_amount:
                    ordered_item = int(input("How many would you like to order? "))
                    if ordered_item > count:
                        print(f"Error: the requested amount exceeds the maximum amount available.\nThe maximum amount that can be ordered is {count}.")
                        print()
                        max_amount = input("Would you like to order the maximum amount? (Y/N) ")
                        if max_amount == "Y":
                            print(f"{user_item} ordered: {count}")
                            valid_amount = True
                        else:
                            valid_amount = False
                    elif ordered_item < count:
                        print(f"{user_item} ordered: {ordered_item}")
                        valid_amount = True
        else:
            pass
        valid_input = True
    elif user_input == 3:
        valid_input = True
    else:
        print("Error. Please enter a valid input (1-3).")
        valid_input = False

print()
print(f"Thank you for your visit, {name}!")
