# variable is a container for a value, behaves as the values it contains

#first_name = "abdullah"
#last_name = "nasir"
#print(first_name + last_name)

# variable is a container for a value, behaves as the values it contains

first_name = "abdullah"
last_name = "nasir"
full_name = first_name + " " + last_name
print("Hello "+full_name)

age = 18
#age = age + 1
#print(age)

age += 1
print(age)

print(type(age))

#you can only use int data type for math functions
#print("your age is: "+age)
#the above line will not work because TypeError: can only concatenate str (not "int") to str

#the int data type stores a whole integer number

#covert variable of int data type to str
print("your age is: "+str(age))
#output: your age is: 20

age += 2

print("your age is: "+age)