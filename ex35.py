from sys import exit # exit() fn is used to get out from an infinity loop

def gold_room(): # Defining a fn
    print("This room is full of gold. How much do you take?")

    next = input("> ") # ip er value next e rakhbo
    if "0" in next or "1" in next:
        how_much = int(next) # next er int value how_much e rakha holo
    else:
        dead("Man, learn to type a number.") # next jodi 0/1 na hoy tahole eta print korbe

    if how_much < 50:
        print("Nice, you are not greedy . you win.")
        exit(0) # condition fill hole ekhanei shesh hobe. else e jabe na
    else:
        dead("You greedy bastard.")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input(" >") # next ekta variable jeta ip nite use hocche.

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it , whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next = input(" > ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty.")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job.")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve. ")


start() # eta shurute run hobe.