# tic tac toe

import os, sys
from random import randint
from colors import Colors


# if running on windows, set colors for that
if sys.platform.lower() == "win32":
    os.system('color')

board = []
game = True

def init():
    print(Colors.bg.lightcyan, " " * 28)
    print(Colors.bg.lightmagenta, " " * 28)
    print(Colors.bg.lightwhite, Colors.fg.black, "       TIC TAC TOE         ")
    print(Colors.bg.lightmagenta, " " * 28)
    print(Colors.bg.lightcyan, " " * 28)
    print(Colors.bg.blue, Colors.fg.lightwhite, "       (c) 2020 aki        \n")
    print(Colors.reset)

def winGame(message):
    print()
    print(Colors.bg.green, Colors.fg.lightwhite, "Congratulations! You have won the game!  ")
    print(Colors.reset, Colors.fg.pink, message)
    print(Colors.reset)

def looseGame(message):
    print()
    print(Colors.bg.red, Colors.fg.lightwhite, "Computer wins! Bad luck :(  ")
    print(Colors.reset, Colors.fg.pink, message)
    print(Colors.reset)

def gameOver():
    global game
    print(Colors.bg.red, Colors.fg.yellow, "*** GAME OVER! ***", Colors.reset)
    game = False
    return game

def notGameOver():
    global game
    game = False
    return game

def setBoard():
    row1 = []
    row2 = []
    row3 = []

    for position in range(3):
        row1.append(0)

    for position in range(3):
        row2.append(0)

    for position in range(3):
        row3.append(0)

    board.append(row1)
    board.append(row2)
    board.append(row3)
    return board


def playHuman():
    print(Colors.fg.red, "--> Your turn:\n", Colors.reset)

    def inputRow():
        global humanInputRow
        try:
            humanInputRow = int(input("Row (0-2): "))
            if humanInputRow < 0 or humanInputRow > 2:
                print(Colors.fg.red, "--> Please input correct value (0-2)!\n", Colors.reset)
                inputRow()
        except ValueError:
            print(Colors.fg.red, "--> Please input correct value (0-2)!\n", Colors.reset)
            inputRow()

    def inputCol():
        global humanInputCol

        try:
            humanInputCol = int(input("Col (0-2): "))
            if humanInputCol < 0 or humanInputCol > 2:
                print(Colors.fg.red, "--> Please input correct value (0-2)!\n", Colors.reset)
                inputCol()
        except ValueError:
            print(Colors.fg.red, "--> Please input correct value (0-2)!\n", Colors.reset)
            inputCol()

    inputRow()
    inputCol()

    for row in range(3):
        for col in range(3):
            if board[humanInputRow][humanInputCol] == 9:
                print(Colors.fg.red, "\n--> You can't place your stone onto computer's position!")
                print(" --> Please try again...\n", Colors.reset)
                printBoard()
                playHuman()
                return board
            if board[humanInputRow][humanInputCol] == 1:
                print(Colors.fg.red, "\n--> You can't place your stone onto your own position!")
                print(" --> Please try again...\n", Colors.reset)
                printBoard()
                playHuman()
                return board
            elif board[humanInputRow][humanInputCol] == 0:
                board[humanInputRow][humanInputCol] = 1
                print(Colors.fg.cyan, "\n --> Human's turn:    [o]", Colors.fg.lightwhite, "Row =", humanInputRow, ", Col =", humanInputCol)
                return board

def playComputer():
    computerInputRow = randint(0, 2)
    computerInputCol = randint(0, 2)

    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        printBoard()
        print(Colors.fg.lightcyan, "*** It's a DRAW GAME! ***")
        print(Colors.reset)
        sys.exit()

    for row in range(3):
        for col in range(3):
            if board[computerInputRow][computerInputCol] == 9:
                playComputer()
                return board
            elif board[computerInputRow][computerInputCol] == 1:
                playComputer()
                return board
            elif board[computerInputRow][computerInputCol] == 0:
                board[computerInputRow][computerInputCol] = 9
                print(Colors.fg.red, "--> Computer's turn: [x]", Colors.fg.lightwhite, "Row =", computerInputRow, ", Col =", computerInputCol)
                return board

def printBoard():
    print(Colors.fg.green,"\nPlayfield for this turn:\n")
    print(Colors.fg.darkgrey, "    0 1 2")
    # row 0
    newChar = ""
    for char in board[0]:
        if char == 0:
            newChar += ". "
        if char == 1:
            newChar += "o "
        if char == 9:
            newChar += "x "
    print(Colors.fg.darkgrey, "0:", Colors.fg.lightwhite, newChar)

    # row 1
    newChar = ""
    for char in board[1]:
        if char == 0:
            newChar += ". "
        if char == 1:
            newChar += "o "
        if char == 9:
            newChar += "x "
    print(Colors.fg.darkgrey, "1:", Colors.fg.lightwhite, newChar)

    # row 2
    newChar = ""
    for char in board[2]:
        if char == 0:
            newChar += ". "
        if char == 1:
            newChar += "o "
        if char == 9:
            newChar += "x "
    print(Colors.fg.darkgrey, "2:", Colors.fg.lightwhite, newChar)

    print(Colors.reset)

def checkRows():
    # human
    if board[0] == [1,1,1]:
        winGame("You have three in a row 0 [-] (horizontal)")
        notGameOver()

    if board[1] == [1,1,1]:
        winGame("You have three in a row 1 [-] (horizontal)")
        notGameOver()

    if board[2] == [1,1,1]:
        winGame("You have three in a row 2 [-] (horizontal)")
        notGameOver()

    # computer
    if board[0] == [9,9,9]:
        winGame("Computer has three in a row 0 [-] (horizontal)")
        gameOver()

    if board[1] == [9,9,9]:
        winGame("Computer has three in a row 1 [-] (horizontal)")
        gameOver()

    if board[2] == [9,9,9]:
        winGame("Computer has three in a row 2 [-] (horizontal)")
        gameOver()

def checkCols():
    # human
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        winGame("You have three in a col 0 [|] (vertical)")
        notGameOver()

    if board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        winGame("You have three in a col 1 [|] (vertical)")
        notGameOver()

    if board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        winGame("You have three in a col 2 [|] (vertical)")
        notGameOver()

    # computer
    if board[0][0] == 9 and board[1][0] == 9 and board[2][0] == 9:
        looseGame("Computer has three in a col 0 [|] (vertical)")
        gameOver()

    if board[0][1] == 9 and board[1][1] == 9 and board[2][1] == 9:
        looseGame("Computer three 999 in a col 1 [|] (vertical)")
        gameOver()

    if board[0][2] == 9 and board[1][2] == 9 and board[2][2] == 9:
        looseGame("Computer has three in a col 2 [|] (vertical)")
        gameOver()

def checkDiags():
    # human
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        winGame("You have three in a diag [\\]")
        notGameOver()

    if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        winGame("You have three in a diag [/]")
        notGameOver()

    # computer
    if board[0][2] == 9 and board[1][1] == 9 and board[2][0] == 9:
        looseGame("Computer has three in a diag [/]")
        gameOver()

    if board[0][0] == 9 and board[1][1] == 9 and board[2][2] == 9:
        looseGame("Computer has three in a diag [\\]")
        gameOver()

# main loop
init()
setBoard()
while game == True:
    playHuman()
    playComputer()
    checkRows()
    checkCols()
    checkDiags()
    printBoard()
else:
    print("Bye!\n")
    print(Colors.reset)
