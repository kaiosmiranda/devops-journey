"""
Calculates sum, average, min, and max for a series of user-entered numbers.

This script prompts the user to enter numbers repeatedly until `0` is entered.
It then calculates and displays the sum, average, maximum, and minimum of the
entered numbers. The average is formatted to two decimal places. If no numbers
are entered, it prints an "Invalid number" message.
"""
total = 0
count = 0
bigger = None
minor = None

num = int(input("Type a number to total: "))
while num != 0:
    total += num
    count += 1

    #
    if bigger is None or num > bigger:
        bigger = num
    
    if minor is None or num < minor:
        minor = num

    num = int(input("Type a number to total: "))


if count > 0:
    average = total / count
    print("Total = ", total)
    print(f"Average: {average:.2f}")  # com 2 casas decimais    print("Max = ", bigger)
    print("Min = ", minor)
else:
    print("Invalid number")