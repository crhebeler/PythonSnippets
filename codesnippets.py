

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