"""
A simple calculator that performs basic arithmetic operations.

This script prompts the user to enter two numbers and then calculates and
prints their sum, difference, product, quotient, and average. The division
result is formatted to two decimal places.
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
print("Sum =", sum)

subtraction = num1 - num2
print("Subtraction =", subtraction)

multiplication = num1 * num2
print("Multiplication =", multiplication)

division = num1 / num2
print ("Division = {:.2f}".format(division))

average = (num1 + num2) / 2
print("Average =", average)