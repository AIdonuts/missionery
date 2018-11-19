import time
import random

print ('\n' * 40)
print("by 'TIFFANY'")
print()
time.sleep(1)
print ("-------------------")
time.sleep(1)
print ("    Missionary")
time.sleep(1)
print ("-------------------")
print()

time.sleep(2)
print("\nYou are standing in front a towering glass building.")
time.sleep(1)
print("From the distance, you can make out the faint shape of the entrance.")
time.sleep(1)
print("There is nothing but grass plains all around you.")

def security_floor():
    time.sleep(1)
    print("The doors open to a small room full of different panels and buttons.")
    time.sleep(1)
    print("There is a large screen in front of you, turned on to a blinking screen.")
    time.sleep(1)
    print("All around you are rows and rows of countless multi coloured buttons and panels.")
    do_what = input("> ")
    if "go to screen" in do_what or "screen" in do_what or "look at screen" in do_what:
        time.sleep(1)
        print("You stare closely at the screen, and here's what you see.")
    
def maintenance_floor():
    time.sleep(1)
    print("You step out into a dusty room, filled with different cleaning tools.")
    time.sleep(1)
    print("You see a wooden cabinet at the end of the room.")
    time.sleep(1)
    print("A small towel lies beside it on the floor.")

def elevator():
    time.sleep(1)
    print("The doors slide open and you step inside.")
    print()
    time.sleep(1)
    print("[MAIN ELEVATOR]")
    print()
    print("01  Security")
    print("02  Maintenance")
    print("03  Main Office")
    print("04  Laser Testing Area")
    print("05  EcoDome")
    print("06  Observatory")
    print("07  SSS Hangar")
    print("[restricted area for authorized personnel only]")
    print("08  Private Quarters of J.P. Kyman")
    elevator = input(">> ")
    if "1" in elevator or "first floor" in elevator or "01" in elevator or "security floor" in elevator or "security" in elevator:
        security_floor()
    if "2" in elevator or "second floor" in elevator or "02" in elevator or "maintenance floor" in elevator or "maintenance" in elevator:
        maintenance_floor()
         
#continue here##################################################################

def first_floor():
    time.sleep(1)
    print("As you look more closely at the room, you notice an elevator by the wall just beside the computer.")
    time.sleep(1)
    print("The elevator was also made out of glass, causing it to be so subtlely hidden amongst the transparent walls.")
    time.sleep(1)
    print("A silver panel was situated beside the doors of the elevator, with a small red button placed at the center.")
    do_what = input("> ")
    if "button" in do_what or "push button" in do_what:
        elevator()

    elif "clue" in do_what:
                time.sleep(1)
                print("Try to push the button.")
                do_what = input("> ")
                if "button" in do_what or "push button" in do_what:
                    elevator()

    while do_what != "button" or do_what != "push button":
            do_what = input("> ")
            if "button" in do_what or "push button" in do_what:
                elevator()
            elif "clue" in do_what:
                time.sleep(1)
                print("Try to push the button.")
                do_what = input("> ")
                if "button" in do_what or "push button" in do_what:
                    elevator()

def file():
    time.sleep(2)
    print("(reading file)")
    print("     WELCOME TO MISSIONARY")
    print()
    time.sleep(1)
    print("MISSIONARY is a text adventure game of dimensions, lasers, outer space, and other science stuff.\
 In it, you will venture into multiple dimensions of the different constellations,\
 exploring some of the most intriguing and amazing plains in this entire galaxy!")
    print()
    time.sleep(2)
    print("** Note from creator: To move around, type out short and simple commands like 'go forward' or 'take sword' into the arrows\
that look like this '> ', and do not use more than 4 words for each command.**")
    print()
    time.sleep(2)
    print("ALSO: IF YOU GET STUCK OR YOU DON'T KNOW WHAT COMMANDS TO TYPE OUT, SIMPLY TYPE THE WORDS 'clue', AND YOU WILL GET A HINT. BEWARE OF THE FACT THAT YOU ONLY HAVE 5 CLUES THAT YOU CAN USE THROUGHOUT THE GAME.")
    print()
    time.sleep(2)
    print("Good luck on your mission!")
    print("(file closes)")
    do_what = input("> ")
    if "look around" in do_what or "look" in do_what or "look at the room" in do_what or "look around the room" in do_what:
        first_floor()
        
    elif "clue" in do_what:
                time.sleep(1)
                print("Try to look around the room.")
                do_what = input("> ")
                if "look around" in do_what or "look" in do_what or "look at the room" in do_what or "look around the room" in do_what:
                    first_floor()

    while do_what != "look around" or do_what != "look" or do_what != "look at the room" or do_what != "look around the room":
            do_what = input("> ")
            if "look around" in do_what or "look" in do_what or "look at the room" in do_what or "look around the room" in do_what:
                first_floor()

            elif "clue" in do_what:
                time.sleep(1)
                print("Try to look around the room.")
                do_what = input("> ")
                if "look around" in do_what or "look" in do_what or "look at the room" in do_what or "look around the room" in do_what:
                    first_floor()

def intro():
    time.sleep(1)
    print("The computer screen lights up, and it opens up to a single file.")
    time.sleep(1)
    print("You do not see any other files, documents or websites in the computer.")
    do_what = input("> ")

    if "read file" in do_what or "open file" in do_what or "file" in do_what:
        file()

    elif "clue" in do_what:
                time.sleep(1)
                print("Try to open the file or read it.")
                do_what = input("> ")
                if "read file" in do_what or "file" in do_what or "open file" in do_what:
                    file()

    while do_what != "read file" or do_what != "file" or do_what != "open file":
            do_what = input("> ")
            if "read file" in do_what or "file" in do_what or "open file" in do_what:
                file()

            elif "clue" in do_what:
                time.sleep(1)
                print("Try to open the file or read it.")
                do_what = input("> ")
                if "read file" in do_what or "file" in do_what or "open file" in do_what:
                    file()

    ####continue here

def enter_building():
    time.sleep(1)
    print("You enter the building.")
    time.sleep(1)
    print("Inside reveals an empty white room, with only a small, white desk at the very end.")
    time.sleep(1)
    print("There is a single computer on the desk.")
    do_what = input("> ")
    if "computer" in do_what or "turn on computer" in do_what or "go to computer" in do_what or "walk towards computer" in do_what or "go forward" in do_what or "walk forward" in do_what:
        intro()

    elif "clue" in do_what:
                time.sleep(1)
                print("Try to turn on the computer.")
                do_what = input("> ")
                if "computer" in do_what or "turn on computer" in do_what or "go to computer" in do_what:
                    intro()

    elif "destroy computer" in do_what:
        time.sleep(1)
        print("Just what in the dimensions is wrong with you?! Absolutely not!")
        do_what = input("> ")
        if "computer" in do_what or "turn on computer" in do_what or "go to computer" in do_what:
                intro()
                
        elif "clue" in do_what:
                time.sleep(1)
                print("Try to turn on the computer.")
                do_what = input("> ")
                if "computer" in do_what or "turn on computer" in do_what or "go to computer" in do_what:
                    intro()
        

    while do_what != "computer" or do_what != "turn on computer" or do_what != "go to computer":
            time.sleep(1)
            print("Try rephrasing your command in a different way.")
            do_what = input("> ")
            if "computer" in do_what or "turn on computer" in do_what or "go to computer" in do_what:
                intro()
                
            elif "clue" in do_what:
                time.sleep(1)
                print("Try to turn on the computer.")
                do_what = input("> ")
                if "computer" in do_what or "turn on computer" in do_what or "go to computer" in do_what:
                    intro()
                    
do_what = input("> ")
if "go forward" in do_what or "forward" in do_what or "go to building" in do_what or "building" in do_what:
    enter_building()

elif "look around" in do_what or "look" in do_what:
    time.sleep(1)
    print("Your surroundings are all just endless, green grass plains, with no buildings or whatsoever anywhere.")
    time.sleep(1)
    print("The only building is the glass tower up ahead.")
    do_what = input("> ")
    if "go forward" in do_what or "forward" in do_what or "go to building" in do_what or "building" in do_what or "go forward to building" in do_what:
        enter_building()

    elif "clue" in do_what:
        time.sleep(1)
        print("Try to go forward into the building.")
        do_what = input("> ")
        if "go forward" in do_what or "forward" in do_what:
            enter_building()

elif "clue" in do_what:
    time.sleep(1)
    print("Try to go forward into the building.")
    do_what = input("> ")
    if "go forward" in do_what or "forward" in do_what:
        enter_building()

while do_what != "go forward" or do_what != "forward" or do_what != "go to building" or do_what != "building" or do_what != "go forward to building":
        do_what = input("> ")
        if "go forward" in do_what or "forward" in do_what:
            enter_building()
        elif "clue" in do_what:
            print("Try to go forward.")
            do_what = input("> ")
            if "go forward" in do_what or "forward" in do_what:
                enter_building()
            

