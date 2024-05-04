#Imani Hollie 02/21/2024
#Ch.7 - Input Valdation

#There are no new language features introduced in this chapter.
#Here is a Python version of the psuedocode Program 7-2.
#The program shown in Program 7-4 uses an input validation
#that the value entered by the user is not negative.

#Program 7-4 calculates retail prices.
#MARK_UP us used as a global constant for the markup percentage.
MARK_UP = 2.5
#The main() function.
def main():
    #Variable to control the loop.
    another = 'y'
    #Process one or more items.
    while another == 'y' or another == 'Y':
        #Display an item's retail price.
        showRetail()
        #do this again?
        another = input('Do you have another item? ' + '(Enter y for yes): ')
#The showRetail() function gets an item's wholesale cost and
#displays the item's retail price.
def showRetail():
    #Get the item's wholesale cost.
    wholesale = float(input('Enter the item\'s wholesale cost: '))
    #Validate the wholesale cost
    while wholesale < 0:
        print('ENTER: The cost cannot be negative.')
        wholesale = float(input('Enter the correct wholesale cost: '))
        #Calculate the retail price.
        retail = wholesale * MARK_UP
        #Display the retail price.
        print('The retail price is $', format(retail, '.2f'))
        #Call the main function
        main()