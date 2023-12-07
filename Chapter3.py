# Bryan Ulloa
# 11/30/23

# Chapter 3 will be introduced.
import time

def Chapter3():
    time.sleep(2)
    print("Welcome to Chapter 3!")
    time.sleep(3)
    # Asking the user how they are feeling
    nervousness = int(input("On a scale of 1 through 5, how nervous are you feeling? "))

    if 1 <= nervousness <= 5:
        print(f"You're feeling {nervousness} out of 5 nervous.")
        time.sleep(2)
        # The heist is ready to begin
        print("You enter the bank and lock the doors behind you.")
        time.sleep(3)
        # Giving the player 2 options
        print("You now have two options:")
        print("1 - Tell everyone it's a robbery and instruct them to put their hands up.")
        print("2 - Threaten people with your weapon and shoot once up in the air.")
        time.sleep(2)
        choice = input("Which option do you choose? ")
        # This will explain more about option 1
        if choice == '1':
            print("You choose Option 1 - Tell everyone it's a robbery.")
            time.sleep(3)
            print("People start panicking, but most comply with your orders.")
            time.sleep(3)
            print("You tell the bank staff to fill the bag with money.")
            time.sleep(3)
            print("Suddenly, someone triggers the alarm.")
            time.sleep(3)
            print("You can hear sirens in the distance.")
            time.sleep(3)
            print("You run away with the money")

        # This code will explain more about option 2
        elif choice == '2':
            print("You choose Option 2 - Threaten people with your weapon and shoot.")
            time.sleep(3)
            print("The gunshot shocks everyone, and chaos begins in the bank.")
            time.sleep(3)
            print("Some people scream out of fear, while others start running.")
            time.sleep(3)
            print("A security guard attempts to intervene.")
            time.sleep(3)
            print("You're forced to make a quick decision.")
            time.sleep(3)
            print("You run away with the money")
            time.sleep(3)

        else:
            print("Invalid choice.")

    else:
        print("Invalid. Please choose a number between 1 and 5.")
# Finalizing chapter 3
def run_Chapter3():
    Chapter3()  # Chapter3

if __name__ == "__main__":
    run_Chapter3()  # Run the Chapter3 story
