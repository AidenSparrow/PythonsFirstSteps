#slicing = create a substring by extracting elements from another string

#we can use the operator indexing[] or
#we can also use the function slice()

# we have 3 optional arguements to define where and how to slice our string [start:stop:step]

name = "abdullahnasir"

first_name = name[0:8]
last_name = name[8:13]
#in the arguement [o:2] first index (0) is inclusive and the second index (2) is exclusiv, thats why we only get 2 characters
#if the arguement is written as [:2] it will give the same result as python would assume the first character to be (0)
print(first_name+" "+last_name)

#step is an optional value and it determines how much we are increaseing our index by
#by default step is one but we can set it to a different value ourselves
#eg below we are splicing the string from index 0 and 8 and reading every third character
#if the start and stop indexes are empty python will assume them to be the first and last index/character in the string that means 0 and 13
#this also means using the entire string


funky_name = name[0:8:3]
print(funky_name)

#now we will reverse a string by stting step to -1

reversed_name = name[::-1]
print(reversed_name)

#now we will look at the slice() function, used to make a sliced object that is reusable

website = "http://google.com"

website2 = "http://facebook.com"

#make a substring based on the website name only

slice = slice(7,-4)

#remove the http and .com portion of the website

print(website[slice])

#output is "google"

print(website2[slice])

#output is "facebook"
