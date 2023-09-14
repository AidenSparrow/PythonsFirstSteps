# if statement is a block of code that will only execute if its condition is true

#its a form of decision making in programming

# the indented code under "if" is the block of code that will be executed if the condition is true

age = int(input("How old are you?: "))

if age == 100:  #comparison operator "==", single "=" is the assignment operator and it is used to assign a value or a string to a variable
    print("You are a century old!")

elif age >= 18:
    print("You are an adult!")  
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")

#check more than one conditions by using else if statements