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
representing unicode characters

However, Python does not have a character data type, 
a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
Example
Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])  # Output: e
'''
#Looping Through a String
'''
Since  strings are arrays, we can loop through the
characters in a string, with a #for loop
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
'''
#String Lenghth
"""
The len() function returns the length of a string:
Example:
a = "Hello, World!"
print(len(a))   # Output:  13
"""

#Check String
'''
To check if a certain phrase or character is 
present in a string, we can use the keyword in.

Example
Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)     #Output: True

***Use it in an if statement:
Example
Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  Output: Yes, 'free' is present
'''
#Check if NOT
'''
To check if a certain phrase or character is 
NOT present in a string, we can use the keyword 
not in.
Example:
txt = "The best things in life are free
but not all things come for free."
print("expensive" not in txt)
Output: True

***Use it in an if statement:

Example
print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
print("No,'expensive' is NOT present.")
Output: No,'expensive' is NOT present
'''
#Pyyhon -Slicing Strings
#Slicing
"""
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, 
to return a part of the string.

ExampleGet your own Python Server
Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])
Output: llo

***NOTE// The first character has index 0.
"""
#Slice From the Start
'''
Get the characters from the start to position 5 (not included):
b =  "Hello, World!"
print(b[:5])
Output: Hello
'''
#Slice To the End
'''
By leaving out the end index, the range will go to the end:

Example:
Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])
Output: llo, World!
'''

#Negative Indexing
'''
Use negative indexes to start the  slicing from the end  of the string:
Example:
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):'''
b = "Hello, World!"
print(b[-5:-2])
#Output: orl


#Python Modifying Strings
'''Python has a built-in methods that can use on strings'''

#Upper Case
'''
The upper() methods returns the string in upper case:'''
#Example:
a = "Hello, World!" 
print(a.upper()) 
#Output: HELLO, WORLD!

#Lower Case
'''
The lower() method returns the string in lower case'''
a = 'Hello, World!'
print(a.lower())
#Output: hello, world!

#Remove Whitespace
'''
Whitespace is the space before and/or after the actual text,
and very often you want to remove this space.
'''
#Examples:

'''
The strip() method removes any whitespace from the beginning or the end:
'''
a = "   Hello, World!   "
print(a.strip()) # Output: Hello, World!

#Replace String
'''The replace() method replaces a string with another string:'''
a = "Hello, World!"
print(a.replace("World", "Python  ")) 
# Output: Hello, Python!  

#Split  String
'''The split() method returns a list where the text between the 
specified separator becomes the list items.'''
#Example
'''The split() method splits the string into substrings if 
it finds instances of the separator:'''
a = "Hello, World!"
print(a.split(",")) 
# Output: ['Hello', ' World !']

#String Concatenation
'''
To cancatenate, or combine, two strings you can use  + operator
'''
#Example
'''Merge variable a with variable b into variable c:'''
a = "Hello"
b = ", World!"
c = a + b
print(c) 
# Output: Hello,World!

#Example:
'To add a space between them add " ":'
a =  "Hello"
b = ", World!"
c = a + " " + b
print(c)
# Output: Hello, World!

#Python - Format-strings

#String Format
'''we cannot combine strings and numbers like this:
'''
#Example
age = 26
txt = "My name is Queen, I am" + age
print(txt)

'''
But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, 
formats them, and places them in the string 
where the placeholders {} are:
'''
#Example
'''Use the format() method to insert numbers 
into strings'''

age = 26
txt = "My  name is Queen, I am {}"
print(txt.format(age)) 
#Output: My  name is Queen, I am 26

'The format() method takes unlimited number of arguments, and are placed into the respective placeholders:'

#Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

"You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:"
#***(Note that Python uses zero based counting)

#Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#output: I want to pay 49.95 dollars for 3 pieces of item 567

#Python - String Methods
'''
Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. 
They do not change the original string.


Method	           Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''

#Python - Escape Characters
'''
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
'''
#Example
x = "I said \"Hello\""
y = 'I said "Hello"' #This would cause a syntax error because Python
print(x) # Output: I said  "Hello"
print(y) # Output: SyntaxError:
#Solution
x = "I said \"Hello\""
y = 'I said \'Hello\''
print(x) # Output: I said "Hello"
print(y) # Output: I said 'Hello'

#Escape Characters
#Other escape characters used in Python:
'''
Code	Result	
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''
