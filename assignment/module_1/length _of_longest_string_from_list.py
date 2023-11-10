#Write a Python function that takes a list of words and returns the length of the longest one.
str1= input("Enter a String : ")

list_of_words = str1.split()

longest_word = max(list_of_words, key = len)
length = len(longest_word)

print("Longest word : ",longest_word)
print("Length of word : ", length)
