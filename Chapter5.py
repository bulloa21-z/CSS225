# Bryan Ulloa
# 12/2/2023

# This code will introduce Chapter 5

import time

def Chapter5():
    # Telling the player that Chapter 5 is beginning
    time.sleep(1)
    print("Chapter 5: The Escape")
    time.sleep(3)
    # The story continues
    print("You slowly regain consciousness in a hospital room.")
    time.sleep(3)
    # The player will play it safe
    print("Looking around, you see a security guard standing outside your room, making sure you go nowhere.")
    time.sleep(4)
    # Telling the player that they are in trouble
    print("Your wrist is handcuffed to a chair .")
    time.sleep(4)
    # There is a solution to the problem
    print("As you attempt to scape n, you notice something on the bedside table - a paper clip!")
    time.sleep(4)
    # Give the player a choice if they want to use the paperclip or no
    choice1 = input("Will you attempt to escape using the paperclip? (Yes/No): ").lower()

    if choice1 == 'no':
        print("Feeling trapped, you won't try using the paperclip.")
    elif choice1 != 'yes':

        print("Not seeing any other way out, you decide to try using the paperclip.")
    else:

        print("Deciding to take your chances, you grab the paperclip to attempt your escape.")
    time.sleep(4)

    print("With a little effort and some luck, you manage to pick the lock and free yourself from the handcuffs!")
    time.sleep(4)

    print("However, the sound of the security guard startles you.")
    time.sleep(3)

    choice2 = input("Will you confront the security guard or try to evade? (y/n): ").lower()
        # Player chose option number 2
    if choice2 == 'n':
        print("You duck into a nearby room, trying to avoid the security guard.")
        time.sleep(3)

        print("You run down the hospital corridor, you find an exit and escape into the night.")
        time.sleep(4)

        print("Making your way back to your apartment, you quickly pack your belongings.")
        time.sleep(3)

        country_choice = input("Which country will you flee to? ")
        time.sleep(3)

        print(f"You are ready to flee to {country_choice}, your new journey awaits.")
        time.sleep(3)
        # Congratulating the player for their escape
        print("Congratulations on your escape!")

    elif choice2 == 'y':
        print("You prepare to confront the security guard 1 on 1.")
        time.sleep(3)

        print("You take him down and he falls, he's knocked out.")
        time.sleep(3)

        print("Taking the guard down, you make an escape from the hospital.")
        time.sleep(4)

        print("Rushing back to your apartment, you quickly gather your essentials.")
        time.sleep(3)

        country_choice = input("What country will you flee to? ")
        time.sleep(3)
        # player will decide where they will like to flee to.
        print(f"Deciding to find a new life in {country_choice}, you prepare for a fresh start.")
        time.sleep(3)

        print("Congratulations on your escape!")
        # Print have a good time
        ascii_art = '''
         |_|  _.     _     _.    _   _   _   _|   _|_ o ._ _   _  
         | | (_| \/ (/_   (_|   (_| (_) (_) (_|    |_ | | | | (/_ 
                                 _|                                
        '''
        print(ascii_art)

    else:
        print("Feeling unsure, you're suddenly pushed into a fight with the security guard.")
        time.sleep(4)

        print("A fight begins, and you manage to beat the guard, finding an opportunity to run away.")
        time.sleep(4)

        print("Quickly returning to your apartment, you pack your belongings.")
        time.sleep(3)

        country_choice = input("Which country will you flee to? ")
        time.sleep(3)

        print(f"You will try to find refuge in {country_choice}, you find a new life.")
        time.sleep(3)
    # Thank the player and congratulate them
        print("Congratulations on your escape!")
# Printing for the player to have a good time
        ascii_art = '''
        
         |_|  _.     _     _.    _   _   _   _|   _|_ o ._ _   _  
         | | (_| \/ (/_   (_|   (_| (_) (_) (_|    |_ | | | | (/_ 
                                 _|                                
        '''
        print(ascii_art)

# The ending of Chapter 5 and the game
def run_Chapter5():
    Chapter5()

if __name__ == "__main__":
    Chapter5()
