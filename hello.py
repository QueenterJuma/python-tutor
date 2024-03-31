# import sys
# print(sys.version)

# print("Hello, World!")

#Python Indentation
#Indentation refers to the spaces at the beginning of a code line.
if 5>3:
    print("Five is greater than three")
if 4>2:
    print("Four is also greater than two")

#Python Variables
    """
Variables are containers for storing data values
They must be created before they can be used in
an expression or statement. Variable names cannot start with
a number and can contain letters (A-Z
and a-z), digits (0-9
and underscore _). There are several types of
variables available in Python like local variables, global variables
and built-in variable.
"""
x = 10           #Integer
y = "I am a string"   #
print(type(y))     #To check
#the type of a variable we use
#The type() function returns the type of an
#object along with its value.
#Arithmetic Operators
num1 = 10+5      #
num2 = num1 - 7   #
product = num1 * num2   #
quotient = num1 / num2   #
remainder = num1 % num2
print(f"{num1} + {
    5} = {num1 + 5
          }")
print(f"{num1} - {
    7} = {num2
          }")
print(f"{num1} * {
        num2} = {product}")
print(f"{num1} / {
    num2} = { quotient}")
print(f"{num1} % {
    num2} = { remainder}")
#Assignment operators
num3 = 10
num4 = 3
num3 += 5       #Adds and
#assigns the result to num3
"""
In python, variables are created when you first assign a value to it:

x = 12
y = "Hello, there!"
"""

#COMMENTS
# Single-line comment starts with '#' symbol
"""
Multiple lines can be commented using triple quotes '   """
"""
This is a multiple lines comments which spans across
multiple lines and uses three double quotes on each side
of the text.
"""

#Python Data Types
#Built-in DAta Types
"""
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
#Getting the Data Type  
"""
You  can use the type() function to get the data type of any variable like this:
print(type("Hello"))    #Return
<class 'str'>
print(type(10))         #Return
<class 'int'>

x = True
print(type(x))          #Return
<class 'bool'>        #Notice that
#Python treats capitalized words as
#True when used in Boolean context. 
"""
#Setting the Data Type
"""
In Python, the data type is set when you assign a value to a variable:

Example	         Data Type
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
"""
#Python Numbers
"""
There are three numeric types in Python:
int
float
complex
The int() function converts a number or string  
to an integer. If no argument is given,
it returns zero. 
The float() function converts a number or 
string to a floating point number.
argument is supplied it returns zero.
The complex() function creates a complex number.
It takes two arguments: the real part and the
imaginary part. A complex number can be
written with j instead of i. For example,
4 + 3j represents the same number as
4 + 3*j.

"""
#Random Number
"""Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to
make random numbers:

Example
Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1, 10))"""

#Python Casting
"""You can use the int(), float(),
and complex() functions to cast values from one type
to another. The str() function can also be
used to convert a value to a string."""

#ExampleGet your own Python Server

#Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

