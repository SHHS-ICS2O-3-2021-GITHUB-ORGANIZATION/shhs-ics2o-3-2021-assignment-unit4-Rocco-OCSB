# Author: Rocco Crupi

choice = 0

while choice != 3:
    print ("Please make a selection:")
    print("\n(1) Say Something Nice")
    print("(2) Say Something Funny")
    print("(3) Exit Program")
    print("\nPlease Enter Choice:")
    choice = int(input())
    
    if choice == 1:
        print("\n\nSomething Nice\n\n")
        
    elif choice == 2:
     print("\n\nSomething Funny\n\n")
    
    elif choice == 3:
        exit()
    
    else:
        print("\n\nInvalid Choice\n\n")