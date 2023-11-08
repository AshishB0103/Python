#Write a Python program to count the number of characters (character frequency) in a string.
str1=input("Enter any string :")
ch1=input("Enter any character :")

ch_freq=0
for i in str1:
    if ch1==i:
        ch_freq+=1

print(ch_freq)
