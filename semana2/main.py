"""
A menu-driven command-line application using utility functions.

This script provides a user with a menu of options:
1. Sum two numbers.
2. Calculate the average of a list of numbers.
3. Find the highest number in a list.
4. Exit the application.

It imports and uses functions from the `function` module to perform these
calculations. The script first greets the user by name and then enters a
loop to display the menu and process user choices.
"""
# Can be this, more basic
import function
# Can be this, the correct
# from funcoes import soma, average, bigger, salute
# Can be this, but not recommend
# from funcoes import *


name = input("Type your name: ")

function.salute(name)

while True:
    print("Menu:")
    print("1 - Sum two numbers")
    print("2 - Avarage of list")
    print("3 - Highest number on the list")
    print("4 - Out")
    option = input("Choose: ")
    
    if option == "1":
        value1 = float(input("Choose a number 1: "))
        value2 = float(input("Choose a number 2: "))
        
        print("Result: ", function.sum1(value1, value2))
    
    elif option == "2":
        numbers = function.read_numbers()
        print("Avarage: ", function.average(numbers))

    elif option == "3":
        numbers = function.read_numbers()
        print("Highest =", function.bigger(numbers))
    
    elif option == "4":
        print("Going out of functions")
        break
    else:
        print("Option unavailable")