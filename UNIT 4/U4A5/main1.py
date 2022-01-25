# Author: Rocco Crupi

choice = 0

while choice != 3:
    print ("Please make a selection:")
    print("\n(1) What is 2 + 2")
    print("(2) a joke ")
    print("(3) Exit Program")
    print("\nPlease Enter Choice:")
    choice = int(input())
    
    if choice == 1:
        print("\n\nthe answer is 4 \n\n")
        
    elif choice == 2:
     print("\n\n What do you call a pig that does karate\n\n A pork chop\n\n")
    
    elif choice == 3:
        exit()
    
    else:
        print("\n\nInvalid Choice\n\n")