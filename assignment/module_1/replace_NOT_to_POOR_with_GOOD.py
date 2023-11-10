"""Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows
the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string."""

str1="He is not a poor man."

find_not=str1.find("not")
find_poor = str1.find("poor")

if find_poor > find_not and find_not > 0 and find_poor > 0:
    str1 = str1.replace(str1[find_not:(find_poor+4)],"good")
    print(str1)
else:
    print(str1)
