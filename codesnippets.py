

How to print in python 3

print ("Hello ")


adding strings together

print ("Hello ") + ("Christopher") 


some common erros in python

print "Mismatched quotes will cause a SyntaxError'
print Without quotes will cause a NameError

when the string is not closed 
SyntaxError: EOL while scanning a string literal


How to assign variables 
todays_date = "March 31, 2021"


How to do Arithmetic In Python 

Big diffrence from Javascript is you can use modulo operator 
to return remainder
15 % 2   so closes you can get is it divided by two there is a remainder 
of 1 

remainder = 1398 % 11 


Multiplication 
product = 5 * 10


How to update data in python 

money_in_pocket = 100
burger_price = 10.00
sales_tax = .12 * burger_price

burger_price += sales_tax
money_in_pocket -= burger_price

add to variable? 

+=  is the way you add vaule to an exsiting variable

Subtracts a value from the variable and assigns the result to that variable.

Syntax
A -= B

A
Any valid object.
B
Any valid object.
 -=


 example of adding to a variable 

 january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
annual_rainfall += september_rainfall
october_rainfall = 7.20
annual_rainfall += october_rainfall
november_rainfall = 5.06
annual_rainfall += november_rainfall
december_rainfall = 4.06
annual_rainfall += december_rainfall


annual_rainfall varibale consits of all the yearly rainfall data


Strings in Python
Assigning Strings Values

Fruit = "Apple"
Type = "Granny Smith"
Location = "Nebraska, USA"




# Printing the strings stored in Variables

print Fruit
print Type
print Location



How to fix a break in Python so you can use (because Pyton with think ' is the end of a stringapostrophe )


#example here:
'Chris\'s Laptop is running Arch Linux' 

#Index in Python:

# Simular to some other languages Python starts from 0 not 1:

Calling index of letters from a sting 

c = "Christopher"[0]
s = "Chris"[4]


fifth_letter = "Hello"[4]

#Various String Methods in Python:

len() #gets the length of number of charatrs of a string:

Greeting = "Hello"
print len(Greeting) # it would print 5:


lower() #This gets rid of capitalizion in a sting (puts everything to lowercase):

Greeting = "Hello"

print Greeting.lower()

upper()#This makes all letter in string uppercase: 

Greeting = "Hello"

print Greeting.upper()   #You would get HELLO:

my_string = "hello"
print len(my_string)
print my_string.upper()

#Expected output HELLO:

#How to turn non strings into strings:
str() 

pi = 3.14
print str(pi)  #output would be string  "3.14"


# Dot Notation in Python:
#Methods that use dot notations will only work with strings:

String Concatenation

print "Hello " + "I\'m  " + "Christopher"


Explicit String Conversion
#mixing variables and Strings

print "The value of pi is the prime number " + str(3.14)


String Formatting with % in Pyton

The % operator after the string is used to combine a string with variables. 

ou can "pad" it with zeros using %02d. The 0 means "pad with zeros", 
the 2 means to pad to 2 characters wide, 
and the d means the number is a signed integer (can be positive or negative).


string_1 = "Chris"
string_2 = "coding"

print "Hello my name is %s. 'I enjoy  %s." % (string_1, string_2)
#expected output:
Hello my name is Chris. 'I enjoy coding.


#raw iput using 

name = raw_input("What is your name? ")
lastname = raw_input("What is your Last Name? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your last name is %s, " \
"and your favorite color is %s." % (name, lastname, color)

#expected output: Ah, so your name is Chirs, your last name is Hebeler, and your favorite color is Red.


Importing Libaries in Python 


#How to import the date and time in Python: 
from datetime import datetime

#now how to use the libary:

now = datetime.now()
print now  #expected output the current date and time:



from datetime import datetime
now = datetime.now()

print now.year
print now.month
print now.day


print '%02d/%02d/%04d' % (now.month, now.day, now.year)  #expected output 09-09-2018:


from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)


#expected out put09/10/2018 21:42:39:

Control Flow 

Control Flow compareaters 

#Equal to (==):

>>> 2 == 2
True
>>> 2 == 5
False

#Not Equal to(!=):

>>> 2 != 5
True
>>> 2 != 2
False


#Less than(<):

>>> 2 < 5
True
>>> 5 < 2
False

#less than or equal to (<=) :

>>> 2 <= 2
True
>>> 5 <= 2
False

#Greater thank (>):

>>> 5 > 2
True
>>> 2 > 5
False

#Greater than or equal to (>=):

>>> 5 >= 5
True
>>> 2 >= 5
False

 A and B of programing 
 
and, or, and not


Boolean examples in Pyton 

bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True


Boolean Or in pyton !

1 < 2 or 2 > 3 is True;
1 > 2 or 2 > 3 is False


Not
The boolean operator not returns True for false statements and False for true statements.

not False will evaluate to True, while not 41 > 40 will return False

bool_one = not True

bool_two = not 3 ** 4 < 4 ** 3 

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3 ** 2 + 4 ** 2 != 5 ** 2

bool_five = not not False

Order of operations rules in pyton 

not is evaluated first;
and is evaluated next;
or is evaluated last.


You can also use Parentheses () so anything in Parentheses is evualted on its own

bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)


Condiontal statments in python 

#if:

if 8 < 9:  #whitespace imporant with python:
  print "Eight is less than nine!"

#indenting is very important with python:


Simple If else statement in Python 

answer = "Christopher is my name"

def name_check():
    if answer == "Christopher is my name":
        return True
    else:             
        return False       # Make sure this returns False

def location_check():
    if answer == "I live in Orlando Florida":
        return True
    else:             
        return False       # Make sure this returns False



        #else if in Python:
        elif is short for "else if."

example here

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


comparators recap 

5 < 6
6 >= 6
11 == 11
12 != 13

How to ask a user for input to store data in a variable

original = raw_input("Enter a word:")


if else statment to check the length of a word by charaters

original = raw_input("Enter a word:")
if len(original) > 0:
  print original
else:
  print "empty"

  .isalpha() can be used to make sure there only is letters and nothing else


original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print original
else:
  print "empty