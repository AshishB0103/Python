#Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.
a = int(input("Enter any number : "))
b = int(input("Enter any number : "))
c = int(input("Enter any number : "))

total = a + b + c
if (a == b or b == c or c == a):
    print(total * 0)
else:
    print("Sum of all 3 number is :",total)
