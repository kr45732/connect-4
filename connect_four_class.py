import colorama
from colorama import Fore, Style
import time as t
import os


class connectFour:
    def __init__(self, board_height, board_width):
        self.height = board_height
        self.width = board_width
        self.area = board_width * board_height
        self.board = []
        self.create_board()

    def clear(self):
        """Clear the shell/output"""
        clr = os.system("clear")
        clr

    def create_board(self):
        for x in range(self.area):
            self.board.append(" ")
            x

    def check_valid(self, column):
        try:
            if 0 < int(column) <= self.width:
                if self.board[int(column) - 1] == " ":
                    return True
                else:
                    return False
        except:
            return False

    def print_board(self):
        for i in range(1, self.width + 1):
            if i > 9:
                print(" ", i, "", end="")
            else:
                print(" ", i, " ", end="")
        for i in range(self.area):
            if i % self.width == 0:
                print()
            print("|", self.board[i], "|", end="")
        print()

    def place_player_one(self, column):
        for i in range(column - 1, column + self.area - self.width, self.width):
            # Un-docstring for animations (work in progress)
            self.board[i] = Style.RESET_ALL + Fore.RED + "R" + Style.RESET_ALL
            if self.height > 20:
                t.sleep(0.05)
            else:
                t.sleep(0.075)
            self.clear()
            self.print_board()
            self.board[i] = " "

            try:
                if self.board[i + self.width] != " ":
                    self.board[i] = Style.RESET_ALL + Fore.RED + "R" + Style.RESET_ALL
                    break
            except:
                if i == ((int(column) + len(self.board) - self.width) - 1):
                    Style.RESET_ALL
                    self.board[i] = Style.RESET_ALL + Fore.RED + "R" + Style.RESET_ALL
                    break
                else:
                    self.board[i - self.width] = (
                        Style.RESET_ALL + Fore.RED + "R" + Style.RESET_ALL
                    )
                    break

    def place_player_two(self, column):
        for i in range(column - 1, column + self.area - self.width, self.width):
            # Un-docstring for animations (work in progress)
            self.board[i] = Style.RESET_ALL + Fore.YELLOW + "Y" + Style.RESET_ALL
            if self.height > 20:
                t.sleep(0.05)
            else:
                t.sleep(0.075)
            self.clear()
            self.print_board()
            self.board[i] = " "

            try:
                if self.board[i + self.width] != " ":
                    self.board[i] = (
                        Style.RESET_ALL + Fore.YELLOW + "Y" + Style.RESET_ALL
                    )
                    break
            except:
                if i == ((int(column) + len(self.board) - self.width) - 1):
                    Style.RESET_ALL
                    self.board[i] = (
                        Style.RESET_ALL + Fore.YELLOW + "Y" + Style.RESET_ALL
                    )
                    break
                else:
                    self.board[i - self.width] = (
                        Style.RESET_ALL + Fore.YELLOW + "Y" + Style.RESET_ALL
                    )
                    break

    def check_win(self):
        row = self.check_rows()
        column = self.check_columns()
        diagonal = self.check_diagonal()
        if row == "player1" or column == "player1" or diagonal == "player1":
            return "player1"
        elif row == "player2" or column == "player2" or diagonal == "player2":
            return "player2"

    def check_rows(self):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for i in range(1, len(self.board) - self.width + 2, 4):
            list1.append(i)
        for i in range(2, len(self.board) - self.width + 2, 4):
            list2.append(i)
        for i in range(3, len(self.board) - self.width + 2, 4):
            list3.append(i)
        for i in range(4, len(self.board) - self.width + 2, 4):
            list4.append(i)

        for i in range(0, self.height):
            prev1 = ""
            prev2 = ""
            prev3 = ""
            prev4 = ""
            counter = 1
            for x in range(i * self.width, (i + 1) * self.width):
                if counter in list1:
                    prev1 = self.board[x].strip()
                elif counter in list2:
                    prev2 = self.board[x]
                elif counter in list3:
                    prev3 = self.board[x]
                elif counter in list4:
                    prev4 = self.board[x]
                if "R" in prev1 and "R" in prev2 and "R" in prev3 and "R" in prev4:
                    return "player1"
                elif "Y" in prev1 and "Y" in prev2 and "Y" in prev3 and "Y" in prev4:
                    return "player2"
                counter += 1

    def check_columns(self):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for i in range(1, len(self.board) - self.width + 2, 4):
            list1.append(i)
        for i in range(2, len(self.board) - self.width + 2, 4):
            list2.append(i)
        for i in range(3, len(self.board) - self.width + 2, 4):
            list3.append(i)
        for i in range(4, len(self.board) - self.width + 2, 4):
            list4.append(i)
        for i in range(0, self.width):
            prev1 = ""
            prev2 = ""
            prev3 = ""
            prev4 = ""
            counter = 1
            for x in range(i + self.area - self.width, i - 1, -self.width):
                if counter in list1:
                    prev1 = self.board[x]
                elif counter in list2:
                    prev2 = self.board[x]
                elif counter in list3:
                    prev3 = self.board[x]
                elif counter in list4:
                    prev4 = self.board[x]
                if "R" in prev1 and "R" in prev2 and "R" in prev3 and "R" in prev4:
                    return "player1"
                elif "Y" in prev1 and "Y" in prev2 and "Y" in prev3 and "Y" in prev4:
                    return "player2"

                counter += 1

    def play_game(self):
        self.clear()
        self.print_board()
        while True:
            print(
                "Player one's turn! Piece color - "
                + Style.RESET_ALL
                + Fore.RED
                + "R"
                + Style.RESET_ALL
            )
            while True:
                
                column = input("Choose the column number to place your piece: ")
                if self.check_valid(column):
                    break
                else:
                    self.print_board()
                    print(
                        Style.RESET_ALL
                        + Fore.YELLOW
                        + "Invalid column"
                        + Style.RESET_ALL
                    )
            print()
            column = int(column)
            self.place_player_one(column)
            top = [self.board[i] != " " for i in range(0, self.width)]
            if False not in top:
                print("\nGame over, the board is full. Its a tie!\n")
                break

            check_for_win = self.check_win()
            if check_for_win == "player1":
                self.print_board()
                print(
                    "\n\n"
                    + Style.RESET_ALL
                    + Fore.RED
                    + "Player 1 wins!"
                    + Style.RESET_ALL
                    + "\nGame over!"
                )
                break

            print(
                "Player two's turn! Piece color - "
                + Style.RESET_ALL
                + Fore.YELLOW
                + "Y"
                + Style.RESET_ALL
            )
            while True:

                column = input("Choose the column number to place your piece: ")
                if self.check_valid(column):
                    break
                else:
                    self.print_board()
                    print(Style.RESET_ALL)
                    print(Fore.YELLOW + "Invalid column")
                    print(Style.RESET_ALL)
            print()
            column = int(column)
            self.place_player_two(column)
            top = [self.board[i] != " " for i in range(0, self.width)]
            if False not in top:
                print("Game over, the board is full. Its a tie!\n")
                break

            check_for_win = self.check_win()
            if check_for_win == "player2":
                self.print_board()
                print(
                    "\n\n"
                    + Style.RESET_ALL
                    + Fore.YELLOW
                    + "Player 2 wins!"
                    + Style.RESET_ALL
                    + "\nGame over!"
                )
                break

    def check_diagonal(self):
        for i in range(0, self.height - 3):
            for x in range(0, self.width - 3):
                original_val = self.board[
                    -(i * self.width) + self.width * (self.height - 1) + x
                ]
                if original_val == " ":
                    continue
                val1 = ""
                val2 = ""
                val3 = ""
                for z in range(1, 4):
                    if z == 1:
                        val1 = self.board[
                            -(i * self.width)
                            + self.width * (self.height - 1)
                            + x
                            - (z * (self.width))
                            + z * 1
                        ]
                    elif z == 2:
                        val2 = self.board[
                            -(i * self.width)
                            + self.width * (self.height - 1)
                            + x
                            - (z * (self.width))
                            + z * 1
                        ]
                    elif z == 3:
                        val3 = self.board[
                            -(i * self.width)
                            + self.width * (self.height - 1)
                            + x
                            - (z * (self.width))
                            + z * 1
                        ]
                    if (
                        "R" in original_val
                        and "R" in val1
                        and "R" in val2
                        and "R" in val3
                    ):
                        return "player1"
                    elif (
                        "Y" in original_val
                        and "Y" in val1
                        and "Y" in val2
                        and "Y" in val3
                    ):
                        return "player2"

        for i in range(0, self.height - 3):
            for x in range(self.width - 1, 2, -1):
                original_val = self.board[
                    -(i * self.width) + self.width * (self.height - 1) + x
                ]
                if original_val == " ":
                    continue
                val1 = ""
                val2 = ""
                val3 = ""
                for z in range(1, 4):
                    if z == 1:
                        val1 = self.board[
                            -(i * self.width)
                            + self.width * (self.height - 1)
                            + x
                            - z * (self.width)
                            - z
                        ]
                    elif z == 2:
                        val2 = self.board[
                            -(i * self.width)
                            + self.width * (self.height - 1)
                            + x
                            - z * (self.width)
                            - z
                        ]
                    elif z == 3:
                        val3 = self.board[
                            -(i * self.width)
                            + self.width * (self.height - 1)
                            + x
                            - z * (self.width)
                            - z
                        ]
                    if (
                        "R" in original_val
                        and "R" in val1
                        and "R" in val2
                        and "R" in val3
                    ):
                        return "player1"
                    elif (
                        "Y" in original_val
                        and "Y" in val1
                        and "Y" in val2
                        and "Y" in val3
                    ):
                        return "player2"
