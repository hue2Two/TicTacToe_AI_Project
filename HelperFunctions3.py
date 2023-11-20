import random

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4])
    print('-+-+-+-')
    print(board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8])
    print('-+-+-+-')
    print(board[9] + '|' + board[10] + '|' + board[11] + '|' + board[12])
    print('-+-+-+-')
    print(board[13] + '|' + board[14] + '|' + board[15] + '|' + board[16])
    print("\n")

def spaceIsFree(board, position):
    return board[position] == ' '

def insertLetter(board, letter, position):
    if spaceIsFree(board, position):
        board[position] = letter
        printBoard(board)
        if checkDraw(board):
            print("Draw!")
            exit()
        if checkWin(board):
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(board, letter, position)

def checkWin(board):
    def checkWin(board):
        # Check all rows
        if (board[1] == board[2] == board[3] == board[4] != ' '):
            return True
        elif (board[5] == board[6] == board[7] == board[8] != ' '):
            return True
        elif (board[9] == board[10] == board[11] == board[12] != ' '):
            return True
        elif (board[13] == board[14] == board[15] == board[16] != ' '):
            return True

        # Check all columns
        elif (board[1] == board[5] == board[9] == board[13] != ' '):
            return True
        elif (board[2] == board[6] == board[10] == board[14] != ' '):
            return True
        elif (board[3] == board[7] == board[11] == board[15] != ' '):
            return True
        elif (board[4] == board[8] == board[12] == board[16] != ' '):
            return True

        # Check diagonals
        elif (board[1] == board[6] == board[11] == board[16] != ' '):
            return True
        elif (board[4] == board[7] == board[10] == board[13] != ' '):
            return True

        return False


def checkDraw(board):
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def playerMove(board, player):
    position = int(input("Enter the position for 'O': "))
    insertLetter(board, player, position)

def compMove(board, computer):
    possibleMoves = [position for position, letter in board.items() if letter == ' ']
    if len(possibleMoves) != 0:
        position = random.choice(possibleMoves)
        insertLetter(board, computer, position)
    else:
        print("No more moves left!")
