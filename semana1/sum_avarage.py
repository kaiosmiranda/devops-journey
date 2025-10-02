"""
Calculates the sum and average of a series of numbers entered by the user.

This script repeatedly prompts the user to enter a number. The user can keep
entering numbers until they input `0`, which signals the end of the input
sequence. The script then calculates the total sum and the average of all the
numbers entered (excluding the final `0`). If no numbers are entered, it
prints an "Invalid number" message.
"""
total = 0
count = 0

num = int(input("Type a number to total: "))
while num != 0:
    total = total + num # Tem duas opções para somar, tanto essa como a de baixo.
    count += 1     # Assim quando precisar somar um número a ele, basta ultilizar a de cima ou a de baixo

    num = int(input("Type a number to total: "))

if count > 0:
    average = total / count

    print("Total = ", total)
    print("Average = ", average)
else:
    print("Invalid number")
#