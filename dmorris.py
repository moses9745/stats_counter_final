#Stat counter
#created by: David Morris January 2019
#purpose: Stat counter for work
#co-author: Carter Cornelius

import time

#setting variables:
complete = False
victim = 0
notification = 0


#*** Define Function ***
def user_help():
    print("\nEnter 'new' for a new victim or 'notification' for a new notification.")
    print("Enter 'current' to display current stats.")
    print("Enter 'remove' to prompt options to remove a victim or notification from your stats.")
    print("Enter 'q' to quit and display results")
    print("Enter '?' to display this help\n")
#*** End Function ***


#*** Main Body of Script ***
    #welcome banner:
print ('Welcome, this program will keep your stats! Lets get started >> :')
time.sleep(1)

user_help()             #call user_help function defined above
time.sleep(2)           #2 second pause

while(not complete):    #"while" complete is not "True", loop will reiterate through until user enters 'q' to quit the program

    #get user input:
    print ("\nEntry >> :")
    user_input = input('')

    #************************************************************************************************************************
    #*** Start if, elif, else statement to test userinput variable
    #*
    #*** 'new' increments victim variable
    #*** 'notification' increments notification variable
    #*** 'remove' aims to decrement either victim or notification if user needs to remove a tally
    #***     'remove' will prompt user to enter 'new' or 'notification' to determine which variable needs to be decremented
    #*** 'current' will display the users current stats
    #*** 'q' will exit the while loop, display the users stats, and terminate the program
    #*** '?' will reprint the user_help() function w/ entry options
    #*** Entering any other value will notify user of an Invalid entry and reprint the user_help() function
    #************************************************************************************************************************
    if user_input == 'new':
        print('One new victim added to your stats! Keep up the good work! >> :')
        victim += 1             #increment victim variable + 1 // += operator increases variable by defined value to the right of the operator
        time.sleep(1)
        
    elif user_input == 'notification':
        print('One notification added to your stats! Great job! >> :')
        notification += 1       #increment notification variable + 1 // += operator increases variable by defined value to the right of the operator
        time.sleep(1)
        
    elif user_input == 'remove':
        print("Enter 'new' to remove a victim or 'notification' to remove a notification :")
        user_negate = input('')
        
        #*** Start inner if, elif, else statement to test user_negate variable -- removes victim or notification based on input from user
        if user_negate == 'new':
            victim -= 1         #decrement victim variable - 1 // -= operator decreases variable by defined value to the right of the operator
            
        elif user_negate == 'notification':
            notification -= 1   #decrement victim variable - 1 // -= operator decreases variable by defined value to the right of the operator
            
        else:
              print('Invalid input. Try again.')
        #*** End inner if, elif, else statement that tests user_negate variable
              
    elif user_input == 'current':
        print("\nCurrent stats :")
        print("\nVictims :",victim,"\nNotifications :",notification)
        
    elif user_input == '?':
        user_help()
        
    elif user_input == 'q':
        print("You've entered 'q'. Program will now terminate and print your results.")
        complete = True
        
    else:
        print("Invalid entry. Help Menu will be printed below.\n")
        time.sleep(1)
        user_help()
    #*** End if, elif, else statement testing userinput variable


#*** print calls below execute when user has entered 'q' to quit the program
print('\nGreat work advocate! Here is your stats for today: ')
print("Victims :",victim,"\nNotifications :",notification)

#*** End Main ***
