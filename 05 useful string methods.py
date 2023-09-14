# useful string methods

name = "abdullah"
#name = "200"

#if there are two of the same variavles, the second one will be chosen

#length method > gives the length of the string

#print(len(name))

#find method

print(name.find("a"))
#output is 0 as its the 0th position

print("moving on")

#this will capitalise the first letter
print(name.capitalize())

#this will make everything upper case
print(name.upper())
#for space in the lines
print(" ")

#this will make everything lower case
print(name.lower())

#this will return true or false depeding on our string
print(name.isdigit())

#this will return with a boolean value (true, false) that wheter this string consists of alphabetical characters
print(name.isalpha())

#count the number of characters in a string
print(name.count("l"))

#replace the characters in a string = ("your character", "replace with")
print(name.replace("l", "G"))

#just a unique niche feature in python, display a string multiple times
print(name*5)
