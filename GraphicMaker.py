# Made by Jordan Leich on 6/15/2020

# Imports
import random
import time
import turtle


# Restart area once the graphic is finished
def restart():
    user_restart = str(input("Want to make another graphic design (yes or no): "))
    print()

    if user_restart.lower() == 'yes' or user_restart.lower() == 'y':
        start()

    elif user_restart.lower() == 'no' or user_restart.lower() == 'n':
        print("Ending program...\n")
        time.sleep(3)
        quit()

    else:
        print("Invalid input, restarting choice...\n")
        time.sleep(3)
        restart()


# Actual start of program
print(""""
--Speed Tier List--
1 (slowest speed)
50 (medium speed)
100 (fastest speed)
""")
user_speed = int(input("Choose a speed (1 to 100): "))
print()

if user_speed < 1:
    print("Error caught! Ending program!\n")
    time.sleep(3)
    quit()

elif user_speed > 100:
    print("Error caught! Ending program!\n")
    time.sleep(3)
    quit()

user_loops = int(input("How many loops do you want to create (200 to 500, 360 loops is recommended by default): "))
print()

if user_loops < 200:
    print("Error caught! Ending program!\n")
    time.sleep(3)
    quit()

elif user_loops > 500:
    print("Error caught! Ending program!\n")
    time.sleep(3)
    quit()


# Main graphic used
def graphic1(variable1):
    screen = turtle.Screen()
    screen.clear()
    jordan = turtle.Turtle()
    print()
    bg_color = str(input("Choose a background color (black, gray, white): "))
    print()
    graphic_color = str(input("Choose a graphic color (cyan, red, purple, orange, green, blue, pink): "))
    print()
    print("Enjoy your custom graphic!\n")
    time.sleep(3)
    screen.bgcolor(bg_color)
    jordan.pencolor(graphic_color)
    jordan.speed(user_speed)
    for i in range(user_loops):
        jordan.forward(i)
        jordan.left(variable1)

    time.sleep(2)
    print("Your custom graphic has ended!\n")
    time.sleep(2)
    restart()


# Random generated graphic
def graphic2(number):
    screen = turtle.Screen()
    screen.clear()
    jordan = turtle.Turtle()
    print()
    bg_color = str(input("Choose a background color (black, gray, white): "))
    print()
    graphic_color = str(input("Choose a graphic color (cyan, red, purple, orange, green, blue, pink): "))
    print()
    print("Enjoy your custom graphic!\n")
    time.sleep(3)
    screen.bgcolor(bg_color)
    jordan.pencolor(graphic_color)
    jordan.speed(user_speed)
    for i in range(user_loops):
        jordan.forward(i)
        jordan.left(number)

    time.sleep(2)
    print("Your custom graphic has ended!\n")
    time.sleep(2)
    restart()


# Second portion/start of the program
def start():
    user_choice = int(input("What graphic do you want to create (1, 2, 3, 4, 5, 6, 7 or pick 8 for a random graphic "
                            "generation): "))

    if user_choice == 1:
        graphic1(50)

    elif user_choice == 2:
        graphic1(90)

    elif user_choice == 3:
        graphic1(78)

    elif user_choice == 4:
        graphic1(45)

    elif user_choice == 5:
        graphic1(124)

    elif user_choice == 6:
        graphic1(167)

    elif user_choice == 7:
        graphic1(132)

    elif user_choice == 8:
        number = random.randint(100, 301)
        graphic2(number)

    else:
        print("Invalid input, restarting choice...\n")
        start()


# Starts the second portion of the program
start()
