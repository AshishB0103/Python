#Write a Python program to get the Factorial number of given number.
factorial=1
n=int(input("Enter any number: "))

if n<0:
   print("Sorry, factorial does not exist for negative numbers")
elif n==0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n+1):
       factorial=factorial*i
   print("Factorial of",n,"is",factorial)
