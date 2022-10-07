#!/usr/bin/env python3
""" ASCII Art Museum | Jay
    View random numbers of ascii arts """

import os
import random
import sys
import threading
import time

# Import dictionary for ascii art - from a file
from halls import art


# print1by1 function for dramatic effect
def print_text(text, delay=0.04):
    """ Printing text for user"""
    for word in text:
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(delay)


# Intro function introducing the setting
def intro():
    """ Introduction page setting"""
    os.system('clear')  # Start with a fresh screen
    (print_ascii("entrance.txt"))  # Display picture of museum entrance
    input("Press enter to continue...\n>")


# Help function will provide commands when called upon by help input also shown at the intro
def help_option():
    """ Help Menu for user"""
    os.system('clear')
    print('''
    ===============================
        Commands:
        -------------------
        north or north wing
        west or west wing
        east or east wing
        south or south wing
        -------------------
        help or h
        quit or q  
    ===============================
    ''')
    input("Press enter to return\n>")


# Leave function to exit program after user input
def leave():
    """ Function to quit from application """
    print("Are you sure you want to quit? Yes/No")
    quit_query = input('>')
    if quit_query.lower() in ['y', 'yes']:
        print("We hope you enjoyed the ASCII Museum!\nExiting...\n")
        sys.exit()
    else:
        pass


# Gaze function runs to view the art for a limited time only, then returns to menu
def gaze():
    """ Showing/waiting time in a ascii art"""
    time.sleep(4.0)
    print_text('Committing the piece\'s glory... You look away with fleeting smile... \n')
    time.sleep(1.5)
    os.system('clear')  # Will clear the screen


S = threading.Timer(5.0, gaze)  # 5 seconds to look upon the lovely art


# Printing ascii function to display the art
def print_ascii(file):
    """ Printing ascii art from a file"""
    with open(file, "r", encoding="utf8") as open_art:
        print(''.join(line for line in open_art))


# Interface function
def menu_interface():
    """ Main menu for navigation """
    print_ascii("hallway.txt")  # ascii picture of museum hall
    print('''
 ====================================================
        Please enter the direction for the wing of 
        the museum you would like to enter:
        ---->  North Wing
        ---->  West Wing
        ---->  South Wing
        ---->  East Wing
 ====================================================
        h  ----> Help,      q  ----> Quit/Exit
        
        ''')


def main():
    """ Main Application Workflow """
    intro()

    while True:
        os.system('clear')
        menu_interface()
        main_input = input("\n>").lower()

        # Go to the north wing
        # if main_input == "north" or main_input == "north wing":
        if main_input in ("north", "north wing"):
            os.system('clear')
            print("Welcome to the North Wing\n\n")
            print_text(
                "You turn your head and look upon an art piece that speaks to you")
            time.sleep(2.0)

            # Start with a fresh screen
            os.system('clear')

            # Slice random ascii art from imported dictionary
            print_ascii(art[0]["north"][random.randint(1, 3)])
            gaze()

        # Go to the west wing
        elif main_input in ("west", "west wing"):
            os.system('clear')
            print("Welcome to the West Wing\n\n")
            print_text(
                "You turn your head and look upon an art piece that speaks to you")
            time.sleep(2.0)

            # Start with a fresh screen
            os.system('clear')

            # Slice random ascii art from imported dictionary
            print_ascii(art[2]["west"][random.randint(1, 3)])
            gaze()

        # Go to the south wing
        elif main_input in ("south", "south wing"):
            os.system('clear')
            print("Welcome to the South Wing\n\n")
            print_text(
                "You turn your head and look upon an art piece that speaks to you")
            time.sleep(2.0)

            # Start with a fresh screen
            os.system('clear')

            # Slice random ascii art from imported dictionary
            print_ascii(art[3]["south"][random.randint(1, 3)])
            gaze()

        # Go to the east wing
        elif main_input in ("east", "east wing"):
            os.system('clear')
            print("Welcome to the East Wing\n\n")
            print_text(
                "You turn your head and look upon an art piece that speaks to you")
            time.sleep(2.0)

            os.system('clear')  # Start with a fresh screen

            # Slice random ascii art from imported dictionary
            print_ascii(art[1]["east"][random.randint(1, 3)])
            gaze()

        # Quit feature using the leave func
        elif main_input in ("quit", "q"):
            os.system('clear')
            leave()

        # Help feature to display commands user can input
        elif main_input in ("help", "h"):
            help_option()

        else:
            os.system('clear')  # Start with a fresh screen
            print("Please enter a valid input")
            time.sleep(0.9)


if __name__ == "__main__":
    main()
