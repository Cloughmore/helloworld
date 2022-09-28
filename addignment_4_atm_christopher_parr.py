"""
Assingment 4
version 1.0
Author: Christopher Parr
23/07/22
"""
#inport statemnts
import sys

correct_pin = 1234 #correct pin value
attempt = 1 #input attempt start value
user_input = 0 #user input default value

#note: there is no error catching set up

print ('') #extra line to make the outpul look nicer

#Gets the users input and checks how many attempts at giving the input they
#have given
for attempt in range (user_input, attempt+2, attempt):
    user_input = int(input('Please enter your pin: '))
    print ('')

    #Account output
    if user_input == correct_pin:
        print ('Welcome to your account.')
        print ('Your account balance is: 0')
        sys.exit()
    #Account blcoked notice
    elif  user_input != correct_pin and attempt == 2:
        print ('Three incorrect attempts logged. Account locked.')
        print ('Your IP has been logged and the police have been notified.')
        sys.exit ()
    #Invalid attempt notice
    elif user_input != correct_pin and attempt < 2:
        print ('Invalid pin.')
        print ('')
