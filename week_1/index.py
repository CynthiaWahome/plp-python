#!/usr/bin/python3

if True:
    print("This is indented properly")


age = int(input("How old are you? "))

if age >= 20: 
    print("You are an adult")
elif age > 12:
    print("You are a teenage") 
else:
    print("You are a child")


def greet(name):
    return f"Hello, {name}!"

print(greet("Angelina"))

