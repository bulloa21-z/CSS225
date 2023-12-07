# Bryan Ulloa
# 11/29/2023

# main.py

import time
import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5
def main():
    print("Robbery - Chapter 1")
    time.sleep(1)
    Chapter1.run_Chapter1()  # Call Chapter 1

    # Move to Chapter 2
    print("\nRobbery - Chapter 2")
    time.sleep(1)
    Chapter2.run_Chapter2()

    # Move to Chapter 3
    print("\nRobbery - Chapter 3")
    time.sleep(1)
    Chapter3.run_Chapter3()

    # Move to Chapter 4
    print("\nRobbery - Chapter 4")
    time.sleep(1)
    Chapter4.run_Chapter4()  # Call Chapter 4

    # Move to Chapter 5
    print("\nRobbery - Chapter 5")
    time.sleep(1)
    Chapter5.run_Chapter5()
if __name__ == "__main__":
    main()


