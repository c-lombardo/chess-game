import time

def checkAdjacent(x, y):
    if y == x + 1: #checks if one right
        return True
    elif y == x - 1: #checks if one left
        return True
    elif y == x + 8: #checks if one down
        return True
    elif y == x - 8: #checks if one up
        return True
    elif y == x + 9: #checks if one SE
        return True
    elif y == x + 7: #checks if one SW
        return True
    elif y == x - 7: #check if one NE
        return True
    elif y == x - 9: #check if one NW
        return True
    else:
        return False

def checkPawnMove(x, y):
    if board[x] != "♟" and board[x] != "♙":
        return True
    elif board[x] == "♟" and y == x - 8 and board[y] != "♙": #can move one north if black
        return True
    elif board[x] == "♙" and y == x + 8 and board[y] != "♟": #can move one south if white
        return True
    elif board[x] == "♙" and y == x + 7 and board[y] == "♟": #capture5
        return True
    elif board[x] == "♙" and y == x + 9 and board[y] == "♟": #capture
        return True
    elif board[x] == "♟" and y == x - 7 and board[y] == "♙": #capture
        return True
    elif board[x] == "♟" and y == x - 9 and board[y] == "♙": #capture
        return True
    elif board[x] == "♟" and x >= 48 and x <= 55 and y == x - 16: #can move 2 if first time moving
        return True
    elif board[x] == "♙" and x >= 8 and x <= 15 and y == x + 16: # rt ^
        return True
    else:
        return False

def checkKnightMove(x, y):
    if board[x] != "♞" and board[x] != "♘":
        return True
    elif y == x - 17 or y == x - 15 or y == x + 15 or y == x + 17 or y == x + 9 or y == x + 7 or y == x - 9 or y == x - 7: #8 places where knight can go
        return True
    else:
        return False

def checkRookMove(x, y):
    if board[x] != "♜" and board[x] != "♖":
        return True
    elif x // 8 ==  y // 8: #checks if on same x-axis, for horizontal movement
        if x < y:
            for n in range(y - x - 1):
                if board[n + x + 1] != "W":
                    return False
            return True
        elif x > y:
            for n in range(x - y - 1):
                if board[n + y + 1] != "W":
                    return False
            return True
    elif x % 8 == y % 8: #checks if on same y-axis, for vertical movement
        if x > y:
            for n in range ((x - y) // 8 - 1):
                if board[y + (n + 1) * 8] != "W":
                    return False
            return True
        elif x < y:
            for n in range ((y - x) // 8 - 1):
                if board[x + (n + 1) * 8] != "W":
                    return False
            return True
    else:
        return False
        
def checkBishopMove(x, y):
    if board[x] != "♗" and board[x] != "♝":
        return True
    elif x % 9 == y % 9: #checks if on same NW to SE axis
        if x > y:
            for n in range((x - y) // 9 - 1):
                if board[y + (n + 1) * 9] != "W":
                    return False
            return True
        elif x < y:
            for n in range ((y - x) // 9 - 1):
                if board[x + (n + 1) * 9] != "W":
                    return False
            return True
    elif x % 7 == y % 7: #checks if on same NE to SW axis
        if x > y:
            for n in range((x - y) // 7 - 1):
                if board[y + (n + 1) * 7] != "W":
                    return False
            return True
        elif x < y:
            for n in range ((y - x) // 7 - 1):
                if board[x + (n + 1) * 7] != "W":
                    return False
            return True
    else:
        return False

def checkQueenMove(x, y):
    if board[x] != "♕" and board[x] != "♛":
        return True
    elif x % 9 == y % 9: #checks if on same NW to SE axis
        if x > y:
            for n in range((x - y) // 9 - 1):
                if board[y + (n + 1) * 9] != "W":
                    return False
            return True
        elif x < y:
            for n in range ((y - x) // 9 - 1):
                if board[x + (n + 1) * 9] != "W":
                    return False
            return True
    elif x % 7 == y % 7: #checks if on same NE to SW axis
        if x > y:
            for n in range((x - y) // 7 - 1):
                if board[y + (n + 1) * 7] != "W":
                    return False
            return True
        elif x < y:
            for n in range ((y - x) // 7 - 1):
                if board[x + (n + 1) * 7] != "W":
                    return False
            return True
    elif x // 8 ==  y // 8: #checks if on same x-axis, for horizontal movement
        if x < y:
            for n in range(y - x - 1):
                if board[n + x + 1] != "W":
                    return False
            return True
        elif x > y:
            for n in range(x - y - 1):
                if board[n + y + 1] != "W":
                    return False
            return True
    elif x % 8 == y % 8: #checks if on same y-axis, for vertical movement
        if x > y:
            for n in range ((x - y) // 8 - 1):
                if board[y + (n + 1) * 8] != "W":
                    return False
            return True
        elif x < y:
            for n in range ((y - x) // 8 - 1):
                if board[x + (n + 1) * 8] != "W":
                    return False
            return True
    else:
        return False

def convertFromCoordinates(x):
    if x[0] == "a":
        x = int(x[1]) - 1
    elif x[0] == "b":
        x = int(x[1]) + 7
    elif x[0] == "c":
        x = int(x[1]) + 15
    elif x[0] == "d":
        x = int(x[1]) + 23
    elif x[0] == "e":
        x = int(x[1]) + 31
    elif x[0] == "f":
        x = int(x[1]) + 39
    elif x[0] == "g":
        x = int(x[1]) + 47
    elif x[0] == "h":
        x = int(x[1]) + 55
    return x

def printBoard():
    print("   __1____2_____3_____4_____5_____6_____7______8_")
    print("a |  " +  board[0]  + "    |   " + board[1] + "   |    " + board[2] + "   |    " + board[3] + "    |   " + board[4] + "   |    " + board[5] + "    |    " + board[6] + "    |   " + board[7] + "  |")
    print("   |_____|_____|_____|______|_____|______|______|_____|")
    print("b |  " +  board[8]  + "    |   " + board[9] + "   |    " + board[10] + "   |    " + board[11] + "    |   " + board[12] + "   |    " + board[13] + "    |    " + board[14] + "    |   " + board[15] + "  |")
    print("   |_____|_____|_____|______|_____|______|______|_____|")
    print("c |  " +  board[16]  + "    |   " + board[17]+ "   |    " + board[18]+ "   |    " + board[19] + "    |   " + board[20] + "   |    " + board[21] + "    |    " + board[22] + "    |   " + board[23] + "  |")
    print("   |_____|_____|_____|______|_____|______|______|_____|")
    print("d |  " + board[24]  + "    |   " + board[25] + "   |    " + board[26] + "   |    " + board[27] + "    |   " + board[28] + "   |    " + board[29] + "    |    " + board[30] + "    |   " + board[31] + "  |")
    print("   |_____|_____|_____|______|_____|______|______|_____|")
    print("e |  " + board[32]  + "    |   " + board[33] + "   |    " + board[34] + "   |    " + board[35] + "    |   " + board[36] + "   |    " + board[37] + "    |    " + board[38] + "    |   " + board[39] + "  |")
    print("   |_____|_____|_____|______|_____|______|______|_____|")
    print("f |  " +  board[40]  + "    |   " + board[41] + "   |    " + board[42] + "   |    " + board[43] + "    |   " + board[44] + "   |    " + board[45] + "    |    " + board[46] + "    |   " + board[47] + "  |")
    print("   |_____|_____|_____|______|_____|______|______|_____|")
    print("g |  " + board[48]  + "    |   " + board[49] + "   |    " + board[50] + "   |    " + board[51] + "    |   " + board[52] + "   |    " + board[53] + "    |    " + board[54] + "    |   " + board[55] + "  |")
    print("   |_____|_____|_____|______|_____|______|______|_____|")
    print("h |  " +  board[56]  + "    |   " + board[57] + "   |    " + board[58] + "   |    " + board[59] + "    |   " + board[60] + "   |    " + board[61] + "    |    " + board[62] + "    |   " + board[63] + "  |")
    print("   |_____|_____|_____|______|_____|______|______|_____|")

board = "♖♘♗♕♔♗♘♖♙♙♙♙♙♙♙♙WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW♟♟♟♟♟♟♟♟♜♞♝♛♚♝♞♜"

print("Welcome to Super Chess Fun-Times!")
print("It has the same rules as normal chess, but black goes first.")
time.sleep(2.5)

turn = 1
gameOver = False


while gameOver == False:
    valid1 = False
    valid2 = False

    printBoard()

    if turn == 1:
        print("BLACK TURN")
        turn = 2
    elif turn == 2:
        print("WHITE TURN")
        turn = 1


    while valid1 == False:
        piece = input("What piece would you like to move? ")
        piece = convertFromCoordinates(piece)
        if turn == 2:
            if board[piece] !="♟" and board[piece] != "♜" and board[piece] != "♞" and board[piece] != "♝" and board[piece] != "♛" and board[piece] != "♚":
                print("Please enter a valid input.")
            else:
                valid1 = True
        elif turn == 1:
            if board[piece] !="♙" and board[piece] != "♖" and board[piece] != "♘" and board[piece] != "♗" and board[piece] != "♕" and board[piece] != "♔":
                print("Please enter a valid input.")
            else:
                valid1 = True


    while valid2 == False:
        space = input("Where would you like to move that piece? ")
        space = convertFromCoordinates(space)
        trel = checkAdjacent(piece, space)
        trel2 = checkPawnMove(piece, space)
        trel3 = checkKnightMove(piece, space)
        trel4 = checkRookMove(piece, space)
        trel5 = checkBishopMove(piece, space)
        trel6 = checkQueenMove(piece, space)
        if turn == 2:
            if board[space] == "♟" or board[space] == "♜" or board[space] == "♞" or board[space] == "♝" or board[piece] == "♛" or board[piece] == "♚":
                print("Please enter a valid input.")
            elif board[piece] == "♚" and trel == False:
                print("Please enter a valid input.")
            elif trel2 == False or trel3 == False or trel4 == False or trel5 == False or trel6 == False:
                print("Please enter a valid input.")
            else:
                valid2 = True
        elif turn == 1:
            if board[space] == "♙" or board[space] == "♖" or board[space] == "♘" or board[space] == "♗" or board[piece] == "♕" or board[piece] == "♔":
                print("Please enter a valid input.")
            elif board[piece] == "♔" and trel == False:
                print("Please enter a valid input.")
            elif trel2 == False or trel3 == False or trel4 == False or trel5 == False or trel6 == False:
                print("Please enter a valid input.")
            else:
                valid2 = True

    board = board[0:space]+board[piece]+board[space+1:]
    board = board[0:piece]+"W"+board[piece+1:]


    if "♚" not in board:
         printBoard()
         print("WHITE WINS!!!!!")
         yn = input("Do you want to play again? (y/n) ")
         if yn == "y":
            board = "♖♘♗♕♔♗♘♖♙♙♙♙♙♙♙♙WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW♟♟♟♟♟♟♟♟♜♞♝♛♚♝♞♜"
            turn = 1
         if yn == "n":
           gameOver = True
           print("Thanks for playing")
                 
                 
    if  "♔" not in board:
         printBoard()
         print("BLACK WINS!!!!!")
         yn = input("Do you want to play again? (y/n) ")
         if yn == "y":
           board = "♖♘♗♕♔♗♘♖♙♙♙♙♙♙♙♙WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW♟♟♟♟♟♟♟♟♜♞♝♛♚♝♞♜"
           turn = 1
         if yn == "n":
            gameOver = True
            print("Thanks for playing")
