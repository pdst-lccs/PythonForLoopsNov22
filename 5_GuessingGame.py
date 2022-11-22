#Python Workshop Day 3
#Nov 2022
#Using a for loop - guessing game

import random   #imoprts random module which contains random number generation functions

number = random.randint(1, 10)    #randint is an inbuilt function that generates a random number between 1 and 10 
print(number) # have a sneak peek!

# Initialise a loop counter  
counter = 0

# Loop 3 times
while counter < 3:  

    guess = int(input("Enter a number between 1 and 10: "))  #guess assigned a value based on user input. changes string to integer
    if guess == number:
        print("Correct")
        break # exit the loop immediately!
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

    counter = counter + 1  

print("Goodbye")