"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string. """

str1=input("Enter a string : ")
count=0

for i in str1:
    count=count + 1
    
str2=str1[0:2]+str1[count-2:count]

if len(str1)<2:
    print("Empty string")        
else:
    print("Input : ",str1)
    print("Output : ",str2)

    
