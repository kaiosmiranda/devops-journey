"""
Calculates the area of different geometric shapes based on user input.

This script prompts the user to choose a shape (circle, triangle, or rectangle)
and then asks for the necessary dimensions (e.g., radius, base, height).
It then calculates and prints the area of the selected shape. The script
handles basic input validation to ensure that only numbers are entered for
dimensions.
"""
import math

print("Choose the shape")
print("1 - Circle")
print("2 - Triangle")
print("3 - Rectangle")

try:
    shape = int(input("Option: "))

    if shape == 1:
        radius = float(input("Enter the radius: "))
        area = math.pi * radius ** 2

        print("Area of circle = {:.2f}".format(area))
    elif shape == 2:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = (base * height) / 2

        print("Area of triangle = {:.2f}".format(area))
    elif shape == 3:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = base * height

        print("Area of rectangle = {:.2f}".format(area))
    else:
        print("Number is not recognized")

except ValueError:
    print("Invalid input! Please enter numbers only.")