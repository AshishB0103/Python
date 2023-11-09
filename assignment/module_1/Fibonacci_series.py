#Write a Python program to get the Fibonacci series of given range.

n = int(input("Enter any number to select a range of a Fibonacci series : "))
n1= 0
n2= 1
n3 = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while n3 < n:
       print(n1)
       n4 = n1 + n2
       n1 = n2
       n2 = n4
       n3 += 1
