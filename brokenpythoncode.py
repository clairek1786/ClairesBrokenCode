#!/usr/bin/python3
number1 = input("Give me a number.")
number2 = input("Give me another number.")
sum = number1 + number2
sum = sum * 2
if sum >= 5:
    print("(" + number1 + " + " + number2 + ") * 2 is greater than 5.")
else:
    print("no")
