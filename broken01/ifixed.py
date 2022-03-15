#!/usr/bin/env python3
'''A program that prompts a user for two operators and operation (plus or minus)
   the program then shows the result.
   The user may enter q to exit the program.'''

calc1 = ""
calc2 = ""
operation = ""
response = ""

while response != "q":
    response = input("\nWhat is the first number? Or, enter q to quit: ")
    calc1 = response
    if calc1 == "q":
        break
    calc1 = float(calc1)
    response = input("\nWhat is the second number? Or, enter q to quit: ")
    calc2 = response
    if calc2 == "q":
        break
    calc2 = float(calc2)
    operation = input("Enter an operation to perform on the two numbers (+ or -): ")
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")

