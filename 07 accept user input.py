#learn to accept user input in python
#asks for you name
#here your name is a string assigned to the variable "name"


name = input("What is your name?: ")

print(name)

#make it better

name = input("What is your name?: ")

print("Hello "+name)

#accept user imput as an int for a math function

age = int(input("How old are you?: "))

height = float(input("How tall are you?: "))

age = age + 1

print("You are "+str(age)+" years old")
print("You are "+str(height)+" centimeter tall")
