from data import stock
from tabulate import tabulate

#  Creating a new list for items only in warehouse 1
warehouse_1 = []
for warehouse_1_item in stock:
    if warehouse_1_item['warehouse'] == 1:
        warehouse_1.append(warehouse_1_item)

#  No. of items in warehouse 1
total_warehouse_1 = len(warehouse_1)

#  Creating a new list for items only in warehouse 2
warehouse_2 = []
for warehouse_2_item in stock:
    if warehouse_2_item['warehouse'] == 2:
        warehouse_2.append(warehouse_2_item)

#  No. of items in warehouse 2
total_warehouse_2 = len(warehouse_2)

#  Function for case insensitive search in stock
#  By converting both items in list
def check_stock():
    for item in warehouse_1:
        if user_item.lower() == warehouse_1["state".lower(), "category".lower()]:
            return True
        else:
            return False

# Function to transform str input into a list
def Convert(string):
    li = list(string.split(" "))
    return li

#  Username input + welcome message
username = input("Hello! What's your username? ")

print(f"Welcome, {username}!")

#  Showing list of options
print(
"What would you like to do?", 
"1. List all items", 
"2. Search an item and place an order", 
"3. Browse by category"
"4. Quit", sep="\n"
)

valid_input = False
while not valid_input:  #  This way the user gets back to the choice selection if they enter an invalid input
    user_input = int(input("Please select your choice by entering its corresponding number: "))
    
    #  CHOICE 1
    if user_input == 1:
        print("\nITEMS IN ALL WAREHOUSES:\n")
        header = stock[0].keys()
        rows = [x.values() for x in stock]
        print(tabulate(rows, header))
        print()
        #  Printing total items per warehouse
        print(f"Total items in Warehouse 1: {total_warehouse_1}")
        print(f"Total items in Warehouse 2: {total_warehouse_2}")
        valid_input = True
    
    #  CHOICE 2
    elif user_input == 2:
        anything_else = False
        while not anything_else:  # This way the user gets back to the item selection if they want to order something else
            user_item = input("What is the name of the item? ")
            user_item_list = Convert(user_item)
            print(user_item_list)
            
            # if check_stock():
            #     total_amount = 0
                # warehouse_1_amount = 0
                # for x, y in warehouse_1:
                #     if x["state"] == user_item[0] and y["category"] == user_item[1]:
                #         warehouse_1_amount += 1
                # warehouse_2_amount = 0
                # for x, y in warehouse_1:
                #     if x["state"] == user_item[0] and y["category"] == user_item[1]:
                #         warehouse_2_amount += 1
                # total_amount = (warehouse_1_amount + warehouse_2_amount)
                # print(f"Amount available: {total_amount}")

            # else:
            #     print("Location: Not in stock")
#             count = warehouse1.count(user_item) + warehouse2.count(user_item)
#             print(f"Amount available: {count}")
#             if user_item in warehouse1 and user_item in warehouse2:
#                 print("Location: Both Warehouses")
#             elif user_item in warehouse1:
#                 print("Location: Warehouse 1")
#             elif user_item in warehouse2:
#                 print("Location: Warehouse 2")
#             else:
#                 print("Location: Not in stock")
#             if warehouse1.count(user_item) > warehouse2.count(user_item):
#                 print(f"Maximum availability: {warehouse1.count(user_item)} in Warehouse 1")
#             elif warehouse1.count(user_item) < warehouse2.count(user_item):
#                 print(f"Maximum availability: {warehouse2.count(user_item)} in Warehouse 2")
#             elif warehouse1.count(user_item) == warehouse2.count(user_item):
#                 pass
#             print()
#             if count >= 1:  # If the item doesn't exist, the user gets prompted to either order something else or quit
#                 order_yn = input("Would you like to place an order for this item? (Y/N) ")
#                 valid_amount = False
#                 if order_yn == "Y":
#                     while not valid_amount:  # If the user refuses to order the maximum amount, they get prompted to enter an amount of their choice
#                         ordered_item = int(input("How many would you like to order? "))
#                         if ordered_item > count:
#                             print(f"Error: the requested amount exceeds the maximum amount available.\nThe maximum amount that can be ordered is {count}.")
#                             print()
#                             max_amount = input("Would you like to order the maximum amount? (Y/N) ")
#                             if max_amount == "Y":
#                                 print(f"{user_item} ordered: {count}")
#                                 valid_amount = True
#                             else:
#                                 valid_amount = False
#                         elif ordered_item < count:
#                             print(f"{user_item} ordered: {ordered_item}")
#                             valid_amount = True
#             continue_shopping = input("Would you like to order anything else? (Y/N) ")
#             if continue_shopping == "Y":
#                 anything_else = False
#             else:
#                 anything_else = True
#         valid_input = True

    #  CHOICE 4
    elif user_input == 4:
        valid_input = True
    #  INVALID INPUT
    else:
        print("Error. Please enter a valid input (1-3).")
        valid_input = False

#  GOODBYE
print()
print(f"Thank you for your visit, {username}!")


            # for i in numbers:
            #     for j in i:
            #     count += 1
            #     sum += j