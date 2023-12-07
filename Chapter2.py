# Bryan Ulloa
# 11/30/23

# Chapter 2 will be introduced
import time

def Chapter2():
    print("You have completed Chapter 1. Welcome to Chapter 2!")
    time.sleep(3)
    print("As you think about your next move, you receive a mysterious call.")
    time.sleep(3)
    print("The voice on the other end whispers, 'I know what you're planning...'")
    time.sleep(3)
    print("Your heart is racing.")
    time.sleep(3)
    print("Now, you try to see whether to continue with the robbery or abandon the plan.")
    time.sleep(3)
    choice = input("What will you choose? (1 - Proceed with the plan / 2 - Abandon the plan): ")

    if choice == '1':
        print("You decide to proceed with the plan despite the mysterious call.")
        time.sleep(3)
        print("You gather your gear and head towards the bank.")
        # Continue with the story...

    elif choice == '2':
        print("You choose to abandon the plan, fearing the consequences.")
        time.sleep(3)
        print("You throw everything away and you will try to forget everything about the robbery.")
        # Ending the story...

    else:
        print("Invalid choice. Please choose 1 or 2.")

    print("Continuing Chapter 2!")
    time.sleep(3)
    print(" You will choose a bank to rob")
    print("You have three bank options:")
    time.sleep(5)
    print("1 - Bank of America: 1 security guard, many cameras, police station somewhat close")
    print("2 - Chase Bank: 2 security guards, numerous cameras, police station far away")
    print("3 - Your Local Bank: No security guards, several cameras")

    bank_choice = input("Which bank would you like to rob? ")

    if bank_choice == '1':
        print("You chose Bank of America")
        time.sleep(3)
        print("You decide to checkout the bank to plan the robbery.")
        time.sleep(3)
        print("After watching for a while, you notice the security guard's routine.")
        time.sleep(3)
        print("You plan to get out there during the guard's break time begin the heist.")


    elif bank_choice == '2':
        print("You chose the Chase Bank.")
        time.sleep(3)
        print("You plan a strategy due to the high security at the Chase bank.")
        time.sleep(3)
        print("You spend several days studying the bank's security protocols and the staff .")
        time.sleep(3)
        print("Your plan will include distracting the guards.")
        time.sleep(3)


    elif bank_choice == '3':
        print("You chose the Local Bank.")
        time.sleep(3)
        print("With no security guards, you feel very confident about the robbery.")
        time.sleep(3)
        print("You plan to disable the cameras and begin stealing from the bank.")
        time.sleep(3)


    else:
        print("Invalid choice.")

def run_Chapter2():
    Chapter2()  # Call the Chapter2 function

if __name__ == "__main__":
    run_Chapter2()  # Run the Chapter2 story

def run_Chapter2():
    Chapter2()  # Call the Chapter2 function

#  Chapter2.py
if __name__ == "__main__":
    run_Chapter2()  # Run the Chapter2 story
