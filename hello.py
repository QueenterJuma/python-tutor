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

#Python Strings
"""
A string is a sequence of characters. You can
create strings by enclosing characters in quotes.
There are two types of quotes you can use:
single quotes (' ') or double quotes (" ").
If you need to include a quote within a string
you can use either single or double quotes around it
or escape the quote with a backslash (\).
"""
#Multiline Strings
"""Strings can span multiple lines if they are en
closed in triple quotes ( """ """) or (''' '''). Newlines
are included in the string as \n."""
#Raw Strings
"""Raw strings don’t have any special meaning for
backslashes, so you can include literal back
slashes in them without having to worry about
escaping them. Raw strings are created using
the prefix r instead of the regular prefix. For
example:
r"\n\tHello World!" becomes "\
"""

#Strings are Arrays
"""In Python, strings are arrays of bytes
that encode Unicode characters. If you want
to access individual characters in a string,
you can do so like this:
print(s[0]) # prints first character
print(s[-1]) # prints last character
"""
#Looping Through a String
"""
Since strings are arrays, we can loop 
through the characters in a string, 
with a for loop.
Example
Loop through the letters in the word "banana":

for x in "banana":
  print(x)
  Output: 
  b
  a
  n
  a
  n
  a
  """
#String Length
'''
To get the length of a string, use the len() function.
The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))
Output: 13
'''
#Check String
'''
To check if a certain phrase or character is 
present in a string, we can use the keyword in.
Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)
Output: True

**Use it in an if statement:

Example
Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") #Output: Yes , 'free' is present.
'''
#Check if NOT
'''
To check if a certain phrase or character is NOT present in a string, 
we can use the keyword not in.

Example
Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt) 
Output: True

***Use it in an if statement:

Example
print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  Output: No, 'expensive' is NOT
'''
#PYTHON STRINGS
#Strings
'''A sequence of characters enclosed by double or single quotes (
'' or ") is called a string in Python.
String literal are displayed by print() fuunction

Example:
print("Hello World")
Output: Hello World

print('Hello World')
Output: Hello World
'''
#Assign String to a Variable
'''
Assigning a string to a variable is done with the
 variable name followed by an equal sign 
 and the string

 Example:
 my_string = "This is a string."
 print(my_string)
 Output: This is a string.
'''
#Multiline Strings
'''
You can assign a multiline string to a variable by using three quotes:

Example
You can use three double/single quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
Output: Lorem ipsum dolor sit amet, conse
ctetur adipiscing elit,sed do eiusmod 
tempor incididuntut labore et dolore 
magna aliququa.
'''
#Strings are Arrays
'''
Strings in Python are arrays of bytes 
representingunicode characters

However, Python does not have a character data type, 
a single character is simply a string with a length of 1.

**Square brackets can be used to access elements of the string.
Example
Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])  # Output: e
'''
