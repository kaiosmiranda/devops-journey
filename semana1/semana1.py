import datetime

print("Welcome to my first Python program!")

name = "Kaio"
age = 21

user = input("What is your name? ")

if user == name:
    print("Hello ", user,"- we are the same name!")
else:
    print("Hello", user, "- nice to meet you!")

for i in range(3):
    print("counting", i)

print("Today is", datetime.date.today())