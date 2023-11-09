#Write python program that swap two number with temp variable and without temp variable.
#Swapping with temp variable
a= 10
b= 20

a,b = b,a
print("Value of A is : ",a)
print("Value of B is : ",b)

#Swapping without temp variable
a = int(input("Enter number for A variable : "))
b = int(input("Enter number for B variable : "))

c=a
a=b
b=c

print("Value of A is : ",a)
print("Value of B is : ",b)
