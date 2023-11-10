"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends
with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged."""
str1=input("Enter a string :")

if len(str1)>2:
    print(str1)
    if str1[-3:]=="ing":
        str1+="ly"
    else:
        str1+="ing"
print(str1)

