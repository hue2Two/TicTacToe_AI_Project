import random

# Starting the game
def gameStart_P1():
    print("Welcome to Tic Tac Toe!")
    print("Select board --> 3x3 (enter 1), 4x4 (enter 2): ")

def gameStart_P2():
    userInput = int(input())
    return userInput

# Printing the board
def printBoard(selection, board):
    if selection == 1:
        print(board[1] + '|' + board[2] + '|' + board[3])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[7] + '|' + board[8] + '|' + board[9])
    else:
        print(board[1] + '|' + board[2] + '|' + board[3] + "|" + board[4])
        print('-+-+-+-')
        print(board[5] + '|' + board[6] + '|' + board[7] + "|" + board[8])
        print('-+-+-+-')
        print(board[9] + '|' + board[10] + '|' + board[11] + "|" + board[12])
        print('-+-+-+-')
        print(board[13] + '|' + board[14] + '|' + board[15] + "|" + board[16])

# Check if a space on the board is free
def spaceIsFree(board, position):
    return board[position] == ' '

# Insert a letter in a position on the board
def insertLetter(letter, position, board):
    if spaceIsFree(board, position):
        board[position] = letter
        printBoard(1, board)  # Adjust this if implementing 4x4 board
        if checkDraw(board):
            print("Draw!")
            printBoard(1, board)
            exit()
        if checkForWin(board):
            if letter == 'X':
                print("Bot wins!")
                printBoard(1, board)
                exit()
            else:
                print("Player wins!")
                printBoard(1, board)
                exit()
    else:
        print("Can't insert there!")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position, board)

# Check for a win on the board
def checkForWin(board):
    # Horizontal wins
    if (board[1] == board[2] == board[3] != ' '):
        return True
    elif (board[4] == board[5] == board[6] != ' '):
        return True
    elif (board[7] == board[8] == board[9] != ' '):
        return True
    # Vertical wins
    elif (board[1] == board[4] == board[7] != ' '):
        return True
    elif (board[2] == board[5] == board[8] != ' '):
        return True
    elif (board[3] == board[6] == board[9] != ' '):
        return True
    # Diagonal wins
    elif (board[1] == board[5] == board[9] != ' '):
        return True
    elif (board[3] == board[5] == board[7] != ' '):
        return True
    else:
        return False


# Check for a draw on the board
def checkDraw(board):
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

# Player's move
def playerMove(player, board):
    position = int(input("Enter the position for 'O': "))
    insertLetter(player, position, board)

# Computer's move (bot)
def compMove(bot, board):
    position = chooseRandomMove(board)
    if position is not None:
        insertLetter(bot, position, board)
    else:
        print("No more moves left!")

# Choose a random move for the bot
def chooseRandomMove(board):
    possibleMoves = [position for position, letter in board.items() if letter == ' ']
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
