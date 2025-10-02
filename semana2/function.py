"""A collection of utility functions."""

def salute(name):
    """Prints a welcome message to the user.

    Args:
        name (str): The name of the user to greet.
    """
    print("Welcome,", name)

def sum1(a, b):
    """Calculates the sum of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def average(numbers):
    """Calculates the average of a list of numbers.

    Args:
        numbers (list of int or float): A list of numbers.

    Returns:
        float: The average of the numbers in the list.
    """
    return sum(numbers) / len(numbers)

def bigger(numbers):
    """Finds the largest number in a list.

    Args:
        numbers (list of int or float): A list of numbers.

    Returns:
        int or float: The largest number in the list.
    """
    return max(numbers)

def read_numbers():
    """Reads a list of numbers from user input.

    Prompts the user to specify how many numbers they want to enter,
    then reads each number and returns them as a list.

    Returns:
        list of float: A list of numbers entered by the user.
    """
    count = int(input("How many numbers will be on the list? "))
    numbers = []
    for i in range(count):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)
    return numbers