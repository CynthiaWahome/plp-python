#!/usr/bin/python3

"""

Create a Python program that calculates the average of three exam grades. Instead of hardcoding the grades, prompt the user to input the three grades as float values. The program should then:

1. Calculate the average of the three grades.
2. Print the average as a floating-point number.
3. Print the average as an integer by explicitly converting the float to an integer.

Ensure the program handles the input correctly and performs the required calculations. Ignore any rounding differences when converting the average to an integer.

"""
math = float(input("What is the score in Math? "))

science = float(input("What is the score in Science? "))

geography = float(input("What is the score in Geography? "))



average = (math + science + geography)/3

print("This is the average as a floating point number", average)
print("This is the average as an integer", int(average))