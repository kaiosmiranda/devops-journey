"""
A simple script demonstrating basic loop structures in Python.

This file includes examples of `while` and `for` loops. The active part of the
script prompts the user to enter a number repeatedly. For each number entered,
it prints the double of that number. The loop terminates when the user enters 0,
at which point the program finishes.

The commented-out sections show alternative implementations of a multiplication
table generator using both `while` and `for` loops.
"""

# num = int(input("Number? "))
# x = 0

# while x <= 10:
#     multiplication = num * x
#     print(num, "x", x,"=", multiplication)
#     x = x + 1


# for i in range(11):
#     multiplication = num * i
#     print(num, "x", i,"=", multiplication)
#

num = -1

while num != 0:
    num = int(input("Type a number (0 to out)"))

    if num != 0:
        print("Double", num * 2)
    else:
        print("Program finished.")