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