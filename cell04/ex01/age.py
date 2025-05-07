#!/usr/bin/python3

a = int(input("Please tell me your age :"))
print (f"You are currently {a} years old.")

b = 10
while b <= 30:
    print (f"In {b} years, you'll be {a+b} years old.",end = "\n")
    b += 10

