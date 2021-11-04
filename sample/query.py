from data import stock
from datetime import datetime
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
def check_stock(stock, user_item):
    warehouse_1_count = 0
    warehouse_2_count = 0
    
    '''
    This part checks if the user input is present in stock
    and counts of many instances of them are in it, adding
    them to their respective warehouse count.
    '''
    for x in stock:
        item_name = x["state"] + " " + x["category"]
        if(item_name.lower() == user_item.lower()):
            if x["warehouse"] == 1:
                warehouse_1_count += 1
            if x["warehouse"] == 2:
                warehouse_2_count += 1
    '''
    Printing the total amount available
    '''
    print("Amount available:", warehouse_1_count + warehouse_2_count)
    if (warehouse_1_count + warehouse_2_count) != 0:
        print("Location: ")
        '''
        Printing one line for each item, listing their
        warehouse number + days in stock by subtracting
        the in_stock_since date from today's date.
        '''
        for x in stock:
            item_name = x["state"] + " " + x["category"]
            if(item_name.lower() == user_item.lower()):
                today = datetime.today()
                in_stock_since = datetime.strptime(x["date_of_stock"], "%Y-%m-%d %H:%M:%S")
                days_in_stock = (today - in_stock_since)
                print("- Warehouse", x["warehouse"], "(in stock for", days_in_stock.days, "days)")
        print()
        '''
        Printing the warehouse with the largest amount
        of user_item available at the moment. If the
        value is identical or if the item is not in stock,
        it'll inform the user.
        '''
        if warehouse_1_count > warehouse_2_count:
            print("Maximum availability:", warehouse_1_count, "in Warehouse 1")
        elif warehouse_2_count > warehouse_1_count:
            print("Maximum availability", warehouse_2_count, "in Warehouse 2")
        else:
            print("The product is present in both warehouses in the same quantity.")
    else:
        print("Location: Not in stock.")

# Separate function to extract total amount only
def total_amount(stock, user_item):
    warehouse_1_count = 0
    warehouse_2_count = 0
    '''
    This is the same function as above, I'm only
    extracting this part that calculates the total
    so that I can store the total_amount variable
    and use it in case the user wants to order
    something else other than the first chosen item.
    '''
    for x in stock:
        item_name = x["state"] + " " + x["category"]
        if(item_name.lower() == user_item.lower()):
            if x["warehouse"] == 1:
                warehouse_1_count += 1
            if x["warehouse"] == 2:
                warehouse_2_count += 1
    
    total_amount = (warehouse_1_count + warehouse_2_count)
    return total_amount


#  Username input + welcome message
username = input("Hello! What's your username? ")
print()
print(f"Welcome, {username}!")
print()

#  Showing list of options
print(
"What would you like to do?", 
"1. List all items", 
"2. Search an item and place an order", 
"3. Browse by category",
"4. Quit", sep="\n"
)
print()

valid_input = False
while not valid_input:  #  This way the user gets back to the choice selection if they enter an invalid input
    user_input = int(input("Please select your choice by entering its corresponding number: "))
    print()
    
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
            check_stock(stock, user_item)
            print()
        
        # Asking the user if they want to order
            order_yn = input("Would you like to place an order for this item? (Y/N) ")
            valid_amount = False
            if order_yn == "Y":
                while not valid_amount:  # If the user refuses to order the maximum amount, they get prompted to enter an amount of their choice
                    ordered_item = int(input("How many would you like to order? "))
                    if ordered_item > total_amount(stock, user_item):
                        print(f"Error: the requested amount exceeds the maximum amount available.\nThe maximum amount that can be ordered is {total_amount(stock, user_item)}.")
                        print()
                        max_amount = input("Would you like to order the maximum amount? (Y/N) ")
                        if max_amount == "Y":
                            print(f"{user_item} ordered: {total_amount(stock, user_item)}")
                            valid_amount = True
                        else:
                            valid_amount = False
                    elif ordered_item < total_amount(stock, user_item):
                        print(f"{user_item} ordered: {ordered_item}")
                        valid_amount = True
            continue_shopping = input("Would you like to order anything else? (Y/N) ")
            if continue_shopping == "Y":
                anything_else = False
            else:
                anything_else = True
        valid_input = True
    
    #  CHOICE 3
    
    elif user_input == 3:
        categories = {}
        for x in stock:
            categories.setdefault(x["category"], 0)
            categories[x["category"]] += 1
        
        count = 1
        category_list = []
        for key, value in categories.items():
            print(count, ".", key, "(", value, ")")
            category_list.append(key)
            count += 1
        
        print()
        
        browse_category = int(input("Enter the number of the category you want to browse: "))
        print()
        print("List of", category_list[browse_category -1],"available:")
        
        for x in stock:
            if x["category"] == category_list[browse_category -1]:
                print(x["state"], x["category"], ", Warehouse:", x["warehouse"])
        valid_input = True
        
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
