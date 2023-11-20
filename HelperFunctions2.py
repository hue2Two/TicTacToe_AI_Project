import random

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
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
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(board, mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkDraw(board):
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def playerMove(board, player):
    position = int(input("Enter a position for 'O': "))
    insertLetter(board, player, position)

def compMove(board, computer, player):
    bestScore = -float('inf')
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False, computer, player)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(board, computer, bestMove)

def minimax(board, isMaximizing, computer, player):
    if checkWhichMarkWon(board, computer):
        return 1
    elif checkWhichMarkWon(board, player):
        return -1
    elif checkDraw(board):
        return 0

    if isMaximizing:
        bestScore = -float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False, computer, player)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True, computer, player)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore
