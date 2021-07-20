#importing module for random number generation
import random

#range of the values of a dice
min_val = 1
max_val = 6

#loop through user input
roll_again = "yes"

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are :")
    
    #generating & printing 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
    #generating & printing 2nd random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
    #asking user to roll the dice again. Any input other than yes or y will terminate the loop and stop the game
    roll_again = input("Would you like to roll the dices again?") 
