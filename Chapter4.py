# Bryan Ulloa
# 12/1/2023

# This code will introduce Chapter 4

import time
def Chapter4():
    # using time sleep in this code is essential
    time.sleep(1)
    # Telling the player have have the money but what will happen
    print("You've successfully escaped the bank with the money, ")
    time.sleep(3)
    print("but now you're in a taxi with a bag full of money that suddenly starts beeping.")
    time.sleep(3)
    print("Before you can react, there's an explosion inside the car, and red dye covers everything inside the taxi, including you.")
    time.sleep(3)

    print("The taxi driver can't see anything. Then the taxi driver crashes into some parked cars. ")
    time.sleep(3)
    # Asking the user what they will do after all of this happened
    # The player will have 3 choices
    print("What will you do?")
    time.sleep(3)
    print("1. Get out of the car, run away, and hide in an alleyway.")
    time.sleep(3)
    print("2. Get out of the car and go to the nearest bathroom, which happens to be in a Domino's.")
    time.sleep(4)
    print("3. Get out of the car and run to your nearest friend's house.")
    time.sleep(4)
    user_choice = input("Enter your choice (1-3): ")
    time.sleep(3)
    # The code for option 1
    if user_choice == '1':
        print("You choose to get out of the car, run away, and hide in an alleyway.")
        time.sleep(2)
        print("You find a nearby alley and hide there for a while.")
        time.sleep(2)

        print("While hiding, you hear police sirens approaching. You must decide:")
        time.sleep(2)
        print("A. Stay hidden and wait for the police to leave.")
        time.sleep(2)
        print("B. Try to find a different hiding spot in case the police search the area.")

        choice_A_or_B = input("Enter your choice (A or B): ")

        if choice_A_or_B.upper() == 'A':
            time.sleep(2)
            print("You decide to stay hidden and wait for the police to leave.")
            time.sleep(2)
            print("After some time, the police presence diminishes, and you cautiously leave the alley, contemplating your next move.")
            time.sleep(2)


        elif choice_A_or_B.upper() == 'B':
            print("You try to find a different hiding spot.")
            time.sleep(2)
            print("You move to a different alley, hoping to avoid detection by the police.")
            # printing run
            ascii_art = '''
              _      
             /_/   _ 
            / \/_// /
            '''
            print(ascii_art)

        else:
            print("Invalid choice. You freeze, unsure of what to do.")
    # The code for option 2
    elif user_choice == '2':
        print("You decide to get out of the car and go to the nearest Domino's for the bathroom.")
        time.sleep(2)
        print("You rush into the Domino's bathroom, hoping to clean off the red dye.")
        time.sleep(2)
        print("However, upon entering Domino's, you see a police officer having a meal.")
        time.sleep(2)
        print("What will you do?")
        time.sleep(2)
        print("A. Try to sneak into the bathroom without alerting the officer.")
        time.sleep(2)
        print("B. Leave Domino's and find another place to clean up.")

        choice_A_or_B = input("Enter your choice (A or B): ")

        if choice_A_or_B.upper() == 'A':
            print("You attempt to sneak into the bathroom quietly.")
            time.sleep(2)
            print("You manage to enter the bathroom without drawing the officer's attention.")

            # Continue the story, considering the next steps or potential encounters.

        elif choice_A_or_B.upper() == 'B':
            print("You decide not to risk it and leave Domino's.")
            time.sleep(2)
            print("You exit Domino's and try to find another place to clean off the dye.")

            # Continue the story, searching for a different solution or encountering new challenges.

        else:
            print("You hesitate, unsure of what to do in this situation.")
        # Printing Run
            ascii_art = '''
              _      
             /_/   _ 
            / \/_// /
            '''
            print(ascii_art)
    # This is the option 3
    elif user_choice == '3':
        print("You opt to get out of the car and run to your nearest friend's house.")
        time.sleep(2)
        print("You sprint to your friend's place, hoping for safety and help.")
        time.sleep(2)

        print("When you arrive, you find your friend is not home.")
        time.sleep(2)
        print("What will you do?")
        time.sleep(2)
        print("A. Wait outside your friend's house.")
        print("B. Try to contact your friend using your phone.")

        choice_A_or_B = input("Enter your choice (A or B): ")

        if choice_A_or_B.upper() == 'A':
            print("You decide to wait outside your friend's house.")
            print("After a while, your friend arrives.")

            # Continue the story, discussing the situation with your friend or seeking help.

        elif choice_A_or_B.upper() == 'B':
            print("You try to contact your friend using your phone.")
            print("However, there's no answer.")
        # Printing Run
            ascii_art = '''
              _      
             /_/   _ 
            / \/_// /
            '''
            print(ascii_art)


        else:
            print("You feel stranded, not knowing what to do next.")

    else:
        print("Invalid choice. You feel overwhelmed and you don't know what your next move will be.")

# The end of Chapter 4
def run_Chapter4():
    Chapter4()
if __name__ == "__main__":
    run_Chapter4()
