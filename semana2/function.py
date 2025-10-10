
def salute(name):
    print("Welcome,", name)

def sum1(a, b):
    return a + b

def average(numbers):
    return sum(numbers) / len(numbers)

def bigger(numbers):
    return max(numbers)

# Function to use in the future, so you don't have to repeat the samething in option 2 and 3
def read_numbers():
    count = int(input("How many numbers will be on the list? "))
    numbers = []
    for i in range(count):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)
    return numbers


