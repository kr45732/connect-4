from connect_four_class import connectFour
import sys

print("\nWelcome to connect four, python version!")
while True:
    start_menu = input(
        "Enter 1 for original size game\nEnter 2 for custom size game\nEnter 3 for rules\nEnter 4 to quit\n>> "
    )
    if start_menu == "1":
        print(
            "Original size game selected.\nGame board size is a 7 by 6\nStarting game!"
        )
        width = 7
        height = 6
        break
    elif start_menu == "2":
        width = int(input("Input the width of the board: "))
        height = int(input("Input the height of the board: "))
        print("\nStarting game!")
        
        break
    elif start_menu == "3":
        print("Rules:")
        print(
            "\nTo win Connect Four, all you have to do is connect four of your colored dics pieces in a row. \n\
This can be done horizontally, vertically (or diagonally which is comming in the future). \n\
Each player will drop in one disc piece at a time.\n"
        )
    elif start_menu == "4":
        print("Quitting")
        sys.exit()
    else:
        print("Unknown option\n")


game = connectFour(height, width)

while True:
    game.play_game()
    play_again = input("Play again?('y' or 'n'): ")
    if play_again.lower() != "y":
        break
        
