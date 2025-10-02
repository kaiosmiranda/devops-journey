"""
A simple introductory Python script.

This program serves as a basic demonstration of Python syntax. It greets the
user, prompts for their name, and provides a custom message based on the input.
It also demonstrates a simple `for` loop and prints the current date using the
`datetime` module.
"""
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