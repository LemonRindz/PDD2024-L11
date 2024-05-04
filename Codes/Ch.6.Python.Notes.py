#Imani Hollie 02/14/2024
#Ch.6 - Functions

#Generating Random Integers in Python:
#Python provides several library functions for random numbers.
#To use one, write an 'import' statment first:
#import random
#The first random-number generating function discussed is
#'random.randint' which can be called as shown:
#num = random.randint(1, 100)
#When the function is called, notice the two arguments (1, 100);
#These arguments tell the function to give an int random number in
#the range of 1 - 100 (which are included in the range). When its
#called, it will generate a random number and return that number by
#assigning it to the 'num' variable.

#Writing Your Own Value-Returning Functions in Python:
#In Python, write a value-returning function like a simple function,
#with one exception: A value-returning function must have a 'return'
#statement, which takes the following form:
#def function_name():
    #statement
    #etc.
    #return expression
#The value of the expression that follows the keyword return will be
#sent back to the part of the program that called the function, and
#can be any value, variable, or expression that has a value. Ex:
#def sum(num1, num2):
    #result = num1 + num2
    #return result
#The purpose of the function is to accept 2 integer values as argments
#and to return thier sum. The following statements shows how to call
#the sum function:
#total = sum(2, 3)

#Returning a String From a Python Function:
#You can also write function that return strings. Ex:
#def get_name():
    #Get the user's name
    #name = input('Enter your name:')
    #return the name
    #return name

#Returning a Boolean Value From a Python Function:
#Python allows you to write Boolean Functions, which return either
#True or False. Ex. The following function accepts a number as an agument,
#and returns True if the argument is even; Otherwise it returns False.
#def is_even(num):
    #Determine whether number is even; If it is, set status to true,
    #otherwise set to false.
    #if (num % 2) == 0:
        #status = True
    #else:
        #status = False
    #Return the value of the status variable
    #return status
#The following codes gets a number from the user, and then calls the
#function to determine whether the number is even or odd.
#value = int(input('Enter a number: '))
#if is_even(value):
    #print('The number is even.')
#else:
    #print('The number is odd.')