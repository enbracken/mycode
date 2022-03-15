#!/usr/bin/env python3
"""Alta3 Python Training
   AUthor: Elena Brackenr
   if, elif, else - A simple program using conditionals to make a decision."""

def main():

    message1 = 'You would be a '
    message2 = ' bender!'

    # Question 1: What would you have as a pet?
    # A Dragon
    # B Flying Bison
    # C Otter Penguin
    # D Fire Ferret

    Pet = input('''Find out what Avatar nation you hail from!
What would you have as a pet? Enter a letter:
    A - Dragon
    B - Flying Bison
    C - Otter Penguin
    D - Fire Ferret
    
''')


    # Define Bender style!
    if Pet.upper() == 'A':
        message = message1  + 'Fire' + message2
    elif Pet.upper() == 'B':
        message = message1  + 'Air' + message2
    elif Pet.upper() == 'C':
        message = message1  + 'Water' + message2    
    elif Pet.upper() == 'D':
        message = message1  + 'Earth' + message2
    else:
        message = 'Invalid letter. You are not a bender.'
    
    print(message)

if __name__ == '__main__':
    # Execute when invoked directly
    main()
