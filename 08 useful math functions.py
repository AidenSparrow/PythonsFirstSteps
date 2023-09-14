#lets use some math functions

import math

pi = 3.14

x = 1
y = 2
z = 3

#to round a number to the nearest whole
print(round(pi))
#output = 3

#to round up a number
print(math.ceil(pi))
#output = 4 (it was rounded upto 4)

#round a number down to the nearest whole
print(math.floor(pi))
#output = 3 (it was rounded down to 3)

#absolute value means how far a number is away from zero
print(abs(pi))
#output = 3.14 is 3.14 unit away from zero
#incase of a negative number you will be given a positive value

#pow function raises the value of a number to a power defined
print(pow(pi,2))

#sqrt function is used to find the square root of a number
print(math.sqrt(pi))

#the max function is used to find the largest of a varying amount of values
print(max(x,y,z))
#output = 3

#the same can be done for min value
print(min(x,y,z))

