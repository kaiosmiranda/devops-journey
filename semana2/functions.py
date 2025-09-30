name = input("Type your name: ")

def salute(name):
    print("Welcome,", name)

def sum1(a, b):
    return a + b

def average(numbers):
    return sum(numbers) / len(numbers)

def bigger(numbers):
    return max(numbers)

# Function to use in the future, so you don't have to repeat the samething in option 2 and 3
# def read_numbers():
#     count = int(input("How many numbers will be on the list? "))
#     numbers = []
#     for i in range(count):
#         number = float(input(f"Enter number {i+1}: "))
#         numbers.append(number)
#     return numbers


salute(name)


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
        
        print("Result: ", sum1(value1, value2))
    
    elif option == "2":
        count = int(input("How many numbers will be on the list? "))
        number_list = []

        for i in range (count):
            number = float(input(f"Enter number {i+1}: "))
            number_list.append(number)
        
        print("Avarage: ",average(number_list))

    elif option == "3":
        count = int(input("How many numbers will be on the list? "))
        number_list = []

        for i in range (count):
            number = float(input(f"Enter number {i+1}: "))
            number_list.append(number)
        
        print("Highest =", bigger(number_list))
    
    elif option == "4":
        print("Going out of functions")
        break
    else:
        print("Option unavailable")
