"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2
import pprint
pp = pprint.PrettyPrinter(indent=4)

name = input("Hello! What is your username? ")

print(f"Welcome, {name}!")
print("What would you like to do?", "1. List items by warehouse", "2. Search an item and place an order", "3. Quit", sep="\n")

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
        break
    elif user_input == 2:
        print("")
        valid_input = True
    elif user_input == 3:
        print("")
        valid_input = True
    else:
        print("Error. Please enter a valid input (1-3).")
        valid_input = False

print()
print(f"Thank you for your visit, {name}!")

# YOUR CODE STARTS HERE

# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit
