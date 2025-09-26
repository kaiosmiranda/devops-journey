
# num = int(input("Number? "))
# x = 0

# while x <= 10:
#     multiplication = num * x
#     print(num, "x", x,"=", multiplication)
#     x = x + 1


# for i in range(11):
#     multiplication = num * i
#     print(num, "x", i,"=", multiplication)

num = -1

while num != 0:
    num = int(input("Type a number (0 to out)"))

    if num != 0:
        print("Double", num * 2)
    else:
        print("Program finished.")
    
    