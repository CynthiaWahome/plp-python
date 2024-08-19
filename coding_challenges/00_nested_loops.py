#!/usr/bin/env python3

"""
Nested Loops

Consider a doctor's office schedule. Each appointment is 30 minutes long. A program to print available appointments can use a nested for loop where:

- The outer loop iterates over the hours.
- The inner loop iterates over the minutes.

This program should print times in hours and minutes in the range between 8:00am and 10:00am. 

In this example:

- The outer loop iterates over the time's hour portion between 8 and 9.
- The inner loop iterates over the time's minute portion between 0 and 59.
"""

hour = 8
minute = 0

while hour < 10:
    while minute < 59:
        print(hour, ":", minute)
        minute +=30
    hour += 1
    minute = 0