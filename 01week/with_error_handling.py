#!/usr/bin/env python3

from sys import exit


# user input with error handling
done = False
while not done:
    name = input("What is your name? ")
    if name.isdigit():
        print("Please provide a valid name")
        exit(12) 


    age = input("How old are you? ")
    if age.isalpha():
        print("Please provide a number")
        exit(12) 


    location = input("Where do you live? ")
    if location.isdigit():
        print("Please provide a valid location")
        exit(12)


    print(f'Hello {name}\nYou are {age} years old and you hail from {location}')
