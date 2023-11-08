#Write a Python program to count the occurrences of each word in a given sentence.
str1="Good Afternoon everybody"
word="Good"

x=[]
count=0
x=str1.split(" ")
for i in range(0,len(x)):
    if(word==x[i]):
        count+=1
print("Count of the word :",count)
