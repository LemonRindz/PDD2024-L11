#Imani Hollie 02/28/2024
#Ch.8 - Arrays

#Lists:
#A list is an object that contains multiple data items.
#Each item that is stored in a list is called an element.
#The items that are enclosed in brackets and separated by
#commas are the values of the list elements.
#Here is a statement that creates a list of integers:
    #even_numbers = [2, 4, 6, 8, 10]
#Here is a statement that creates a list if strings:
    #names = ['Molly', 'Steven', 'Will', 'Alicia', 'Adrinana']
#You can use the 'print' function to display an entire list:
    #numbers = [5, 10, 15, 20]
    #print(numbers)

#List Elements and Subscripts in Python:
#You access each element of a list with a subscript.
#The first element's subscript is 0, the second element's
#subscript is 1, etc. The last element's subscript is the array
#size minus 1.
    #numbers = [0, 0, 0]
    #numbers[0] = 10
    #numbers[1] = 20
    #numbers[2] = 30

#Use the 'len' Function with Lists in Python:
#You can use the 'len' function to get the length of a list in Python.
#When you pass a list as an argument the 'len' function returns
#the number of elements in the list. Ex:
    #my_list = [10, 20, 30, 40]
    #index = 0
    #while index < len(my_list):
        #print(my_list[index])
        #index += 1

#Iterating Over a List with the 'for' Loop in Python
#In Python, you can easily iterate over the contents of a list with a
#'for' loop as shown below:
    #numbers = [99, 100, 101, 102]
    #for n in numbers:
        #print(n)

#The variable 'n' is assigned a copy of the first value in the list,
#and then the statements that appear in the block are executed.
#Then, the variable 'n' is assigned a copy of the next value in the list,
#and the block is executed again. This continues until the varible has
#been assigned the last value in the list.

#Keep in mind, that as the 'for' loop executes, the n variable is
#assigned a copy of the list elements, and any changes made to the 'n'
#variable do not affect the list. To demonstrate, look at the following:
    #numbers = [99, 100, 101, 102]
    #for n in numbers:
        #n = 0
    #print(my_list)
#The statement in line 3 reassigns the 'n' variable to a different value.
#It doesn't change the list element that 'n' reffered to beofre the
#statement executed.

#Passing List as an Argument to a function in Python:
#When passing a list as an argument to a function in Python, it is not
#necessary to pass a separate argument indicating the list's size. This is
#because the 'len' function reports the list's size. The following code
#shows a function that has been written to accept a list as an argument:
    #def set_to_zero(numbers):
        #index = 0
        #while index < len(numbers):
            #numbers[index] = 0
            #index = index + 1
#The function's parameter, 'numbers', is used to refer to a list. When you
#call this function and pass a list as an argument, the loop sets each
#element to 0. Ex.
    #my_list = [1, 2, 3, 4, 5]
    #set_to_zero(my_list)
    #print(my_list)

#Two_Dimensional Lists in Python

#Rows and Columns
