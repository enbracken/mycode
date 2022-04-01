#!/usr/bin/env python3

# Read Num File
def numFileImport ():
    Numbers = []
    with open("numfile.txt", "r") as nums:
        Lines = nums.readlines()
    for line in Lines:
        Numbers.append(line)
    return Numbers

# Formatting function
def numFormat():
    Numbers = numFileImport()
    ModNumbers = []
    for number in Numbers:
        number = number.strip('\n')
        number = int(number)
        ModNumbers.append(number)
    return ModNumbers
   # print(ModNumbers)

# Fizz Buzz
def numFizzBuzz():
    # If the element is a multiple of 3, print "Fizz" instead of the number.
    # If the element is a multiple of 5, print "Buzz" instead of the number.
    # If the element is a multiple of both 3 AND 5, print "FizzBuzz" instead of the number.
    # If none of the above are true, just print the number.
    
    numList = numFormat()
    listFB = [] 
    for number in numList:
        Divby3 = number % 3 == 0
        Divby5 = number % 5 == 0

        if Divby3 == True and Divby5 == True:
            listFB.append("FizzBuzz")
        elif Divby3 == True and Divby5 == False:
            listFB.append("Fizz")
        elif Divby5 == True and Divby3 == False:
            listFB.append("Buzz")
        else:
            listFB.append(number)

    print(listFB)
        


if __name__ == "__main__":
   numFizzBuzz()
