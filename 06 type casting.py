#type casting = converting the data type of a value to another data type

x = 1 #integer

y = 2.0 #floating point number as it has a decimal

z = "3" #string as its in double quotations, cannot perform math

y = int(y)

print(x)
print(int(y))
print(z)

#convert y and z into integer data type

print(z*3) #this will not multiply, only print the string 3 times

#now type cast z and perform math

z = int(z)

print(z*3)

#now covert integers to floating point numbers

x = float(x)

#this will display the integer x as a decimal (floating point number)

print(x)

#we cannot print a string and an integer together this is where type casting is useful

print("X is "+str(x))
print("Y is "+str(y))
print(z*3)