#!/usr/bin/python3

num = int(input("Enter a number less than 25 :"))
# if num > 25 :
#     print ("Error")
# while num <= 25 :
#     print (f"Inside the loop, my variable is {num}")
#     num = num+1

if num > 25 :
    print("ERROR")
else :
    for i in range(num,26):
        print(i)