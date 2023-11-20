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

def compMove(board, computer, player):
    print("AI is trying to make a move...")
    bestScore = -float('inf')
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, 0, False, computer, player)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
                print(f"Considering move at {key} with score {score}")

    if bestMove != 0:
        print(f"AI chooses position {bestMove}")
        insertLetter(board, computer, bestMove)
    else:
        print("AI couldn't find a move")

MAX_DEPTH = 4  # Example depth limit

def minimax(board, depth, isMaximizing, computer, player):
    if depth == MAX_DEPTH:  # Define MAX_DEPTH according to your needs
        return 0  # or some heuristic evaluation of the board

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
                score = minimax(board, depth + 1, False, computer, player)
                board[key] = ' '
                bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth + 1, True, computer, player)
                board[key] = ' '
                bestScore = min(bestScore, score)
        return bestScore

def checkWhichMarkWon(board, mark):
    # Check all rows
    for row in range(1, 14, 4):
        if board[row] == board[row + 1] == board[row + 2] == board[row + 3] == mark:
            return True

    # Check all columns
    for col in range(1, 5):
        if board[col] == board[col + 4] == board[col + 8] == board[col + 12] == mark:
            return True

    # Check diagonals
    if board[1] == board[6] == board[11] == board[16] == mark:
        return True
    if board[4] == board[7] == board[10] == board[13] == mark:
        return True

    return False

