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