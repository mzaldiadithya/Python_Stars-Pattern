# ================================== Stars Patern
import os
from time import sleep

boundary = "-------------------------------------"
repeat = "y"

while repeat != "n":
    print("\n\tStars Pattern")

    print(boundary)
    print("1. Evenly Pattern  \n2. Left Quarter Triangle \n3. Left Quarter Triangle (Reverse) \n4. Right Quarter Triangle \n5. Right Quarter Triangle (Reverse) \n6. Half Top Triange \n7. Half Bottom Triangle \n8. Full Triangle")
    print(boundary)

    pattern = int(input("Select The Patern (By Number) : "))

    x = int(input("\nLooping Value : "))

    print(boundary)

    if pattern == 1:
        print("Pattern Selected : 1. Evenly Pattern")
        print()
        for i in range(x):
            for j in range(x):
                print("*", end=" ")
            
            print()

    elif pattern == 2:
        print("Pattern Selected : Left Quarter Triangle")
        print()
        for i in range(x):
            i+=1
            for j in range(i):    
                print("*", end=" ")
            
            print()

    elif pattern == 3:
        print("Pattern Selected : Left Quarter Triangle (Reverse)")
        print()
        for i in range(x,0,-1):
            for j in range(i):    
                print("*", end=" ")
            
            print()

    elif pattern == 4:
        print("Pattern Selected : Right Quarter Triangle")
        print()
        for i in range(x):
            for j in range(i, x-1):
                print(" ",end="")

            for k in range(i+1):
                print("*",end="")

            print()

    elif pattern == 5:
        print("Pattern Selected : Right Quarter Triangle (Reverse)")
        print()
        for i in range(x,0,-1):
            for j in range(i, x+1):
                print(" ",end="")

            for k in range(i):
                print("*",end="")

            print()

    elif pattern == 6:
        print("Pattern Selected : Half Top Triangle")
        print()
        for i in range(x):
            for j in range(i, x-1):
                print(" ",end="")

            for k in range(i+1):
                print("*",end=" ")

            print()

    elif pattern == 7:
        print("Pattern Selected : Half Bottom Triangle")
        print()    
        for i in range(x,0,-1):
            for j in range(i, x):
                print(" ",end="")

            for k in range(i):
                print("*",end=" ")

            print()

    elif pattern == 8:
        print("Pattern Selected : Full Triangle")
        print()    
        for i in range(x):
            for j in range(i, x-1):
                print(" ",end="")

            for k in range(i+1):
                print("*",end=" ")

            print()

        for i in range(x,0,-1):
            for j in range(i, x):
                print(" ",end="")

            for k in range(i):
                print("*",end=" ")

            print()        

    else:
        print("\npattern not found".upper())
            
    print(boundary)

    repeat = input("Want to repeat (y/n) ? ")
    if (repeat == 'y'):
        def clear_screen():
            if os.name == 'posix':
                _ = os.system('clear')
            else:
                _ = os.system('cls')        
        # sleep(1)       
        clear_screen()     
