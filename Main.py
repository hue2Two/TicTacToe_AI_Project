import HelperFunctions
import HelperFunctions2 as AI
import HelperFunctions3 as AI4x4Random
import HelperFunctions4 as AI4x4Minimax

board1 = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

board2 = {1: ' ', 2: ' ', 3: ' ', 4: ' ',
          5: ' ', 6: ' ', 7: ' ', 8: ' ',
          9: ' ', 10: ' ', 11: ' ', 12: ' ',
          13: ' ', 14: ' ', 15: ' ', 16: ' '}

player = '0'
bot = 'X'

HelperFunctions.gameStart_P1()
userInput = HelperFunctions.gameStart_P2()
print(str(userInput) + " was selected!")

if userInput == 1:
    HelperFunctions.printBoard(userInput, board1)

    print("Select computer level 5 or 10: ")
    level = int(input())
    print("You selected " + str(level))

    if level == 5:
        print("Starting game ... ")

        while True:
            HelperFunctions.compMove(bot, board1)
            if HelperFunctions.checkForWin(board1):
                print("Bot wins!")
                break
            elif HelperFunctions.checkDraw(board1):
                print("Draw!")
                break

            HelperFunctions.playerMove(player, board1)
            if HelperFunctions.checkForWin(board1):
                print("Player wins!")
                break
            elif HelperFunctions.checkDraw(board1):
                print("Draw!")
                break
    else:
        print(" starting game ... ")

        # Start of game loop
        while not AI.checkWin(board1):
            AI.compMove(board1, bot, player)
            if AI.checkWin(board1) or AI.checkDraw(board1):
                break
            AI.playerMove(board1, player)

# Other imports and initializations remain the same

else:  # This block is for a 4x4 board
    HelperFunctions.printBoard(userInput, board2)

    print("Select computer level 5 or 10: ")
    level = int(input())
    print("You selected " + str(level))

    if level == 5:
        print("Starting game ... ")
        while True:
            # Player's move
            AI4x4Random.playerMove(board2, player)
            if AI4x4Random.checkWin(board2):
                print("Player wins!")
                break
            if AI4x4Random.checkDraw(board2):
                print("Draw!")
                break

            # Computer's move
            AI4x4Random.compMove(board2, bot)
            if AI4x4Random.checkWin(board2):
                print("Bot wins!")
                break
            if AI4x4Random.checkDraw(board2):
                print("Draw!")
                break


    else:  # For level 10, use Minimax

        print("Starting game ... ")

        while True:

            AI4x4Minimax.playerMove(board2, player)

            if AI4x4Minimax.checkWin(board2):
                print("Player wins!")

                break

            if AI4x4Minimax.checkDraw(board2):
                print("Draw!")

                break

            AI4x4Minimax.compMove(board2, bot, player)

            if AI4x4Minimax.checkWin(board2):
                print("Bot wins!")

                break

            if AI4x4Minimax.checkDraw(board2):
                print("Draw!")

                break


