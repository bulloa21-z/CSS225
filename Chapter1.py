# Bryan Ulloa
# 11/11/23

# Chapter 1 is about to begin
import time

def Chapter1():
    # Ask player for their name and age
    name = input("Hello, what is your name? ")
    # Asking user for their age
    age = input("How old are you, " + name + "? ")
    print("Hello, thief, I mean...")
    time.sleep(2)
    print("Hello, " + name)
    time.sleep(2)
    # Letting them know that they're going to rob a bank
    print("You're going to rob a bank.")
    time.sleep(2)

    ascii_art = '''
             _     _             _                
      /|//_// `   /_)_  _  /_   /_/_  /_ /_ _  _  
     / | / /_,   /_)/_|/ //\   / \/_//_//_//_'//_/
                                               _/ 
    '''
    print(ascii_art)

    time.sleep(2)
    print("You may press the enter key to continue...")
    input("Press Enter to continue...")  # Enter key and the game will begin
    print("You will go to the grocery store to prepare.")
    time.sleep(2)
    # The player will have 3 options for preparation
    print("You can either: ")
    print("\033[34m Option 1 - Buy a bat, one pepper, and a costume disguise\033[0m")
    print("Option 2 - Buy a mask, guns, and a bag")
    print("Option 3 - Buy a knife, a backpack, and spray paint")
    time.sleep(3)
    # Asking the user what they would like to pick
    userOption = input("Which option would you like to pick? ")

    if userOption == '1':
        # Option 1
        print("You chose Option 1 - Buy a bat, one pepper, and a costume disguise")
        time.sleep(2)
        action = input("What do you want to do next? (1 - Go to the bank / 2 - Plan more): ")
        if action == '1':
            print("You decide to go directly to the bank.")
            # Continue the story...
        elif action == '2':
            # Option 2
            print("You choose to plan more before going to the bank.")
            time.sleep(2)
            furtherAction = input("What's your next plan? (1 - Scout some banks / 2 - Go to church and say your last prayers): ")
            if furtherAction == '1':
                print("You decide to scout the bank.")
            elif furtherAction == '2':
                print("You go to church.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")
    elif userOption == '2':
        print("You chose Option 2 - Buy a mask, guns, and a bag")
        time.sleep(2)
        action = input("What's your next move? (1 - Practice at the gun range / 2 - Practice using the gun in your backyard): ")
        if action == '1':
            print("Practice at the gun range.")
            # Will Continue the story...
        elif action == '2':
            print("Practice using the gun in your backyard.")
            # Will Continue the story...
        else:
            print("Invalid choice.")
    elif userOption == '3':
        # Option 3
        print("You chose Option 3 - Buy a knife, a backpack, and spray paint")
        time.sleep(2)
        action = input("What's your strategy? (1 - Plan the robbery / 2 - Gather information on all the banks): ")
        if action == '1':
            print("You plan to rob the bank at day or night.")
            # Will Continue the story...
        elif action == '2':
            print("You gather more information about the banks.")
            # Will Continue the story...
        else:
            print("Invalid choice.")
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

def run_Chapter1():
    Chapter1()

if __name__ == "__main__":
    run_Chapter1()

