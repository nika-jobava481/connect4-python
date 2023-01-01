gameBoard=[[" " for _ in range(6)] for _ in range(7)]
count=0
def printBoard():
    print("_"*57)
    print("    1   |   2   |   3   |   4   |   5   |   6   |   7   |")
    print("+"+"-------+"*7)
    for i in range(6):
        print("|"+"       |"*7)
        print(f"|   {gameBoard[0][i]}   |   {gameBoard[1][i]}   |   {gameBoard[2][i]}   |   {gameBoard[3][i]}   |   {gameBoard[4][i]}   |   {gameBoard[5][i]}   |   {gameBoard[6][i]}   |")
        print("|"+"       |"*7)
        print("+"+"-------+"*7)


printBoard()


def checkWin():
    for i in range(4):
        for j in range(len(gameBoard[i])):
            if gameBoard[i][j]!= " " and gameBoard[i][j]==gameBoard[i+1][j]==gameBoard[i+2][j]==gameBoard[i+3][j]:
                return True
    for col in range(7):
        for i in range(3):
            if gameBoard[col][i] != " " and gameBoard[col][i] == gameBoard[col][i+1] == gameBoard[col][i+2] == gameBoard[col][i+3]:
                return True
    for col in range(4):
        for i in range(3):
            if gameBoard[col][i] != " " and gameBoard[col][i] == gameBoard[col+1][i+1] == gameBoard[col+2][i+2] == gameBoard[col+3][i+3]:
                return True
    for col in range(3, 7):
        for i in range(3):
            if gameBoard[col][i] != " " and gameBoard[col][i] == gameBoard[col-1][i+1] == gameBoard[col-2][i+2] == gameBoard[col-3][i+3]:
                return True
    return False

def putChar(ch,col):
    gameBoard[col][len(gameBoard[col])-gameBoard[col][::-1].index(" ")-1]=ch

def isEmpty(board):
    return any(" " in row for row in board)


while isEmpty(gameBoard):
    char="◯"
    if count%2==1:
        char="●"


    putChar(char,int(input(f"Input column number 1-7 for player {char}:"))-1)
    printBoard()
    if checkWin():
        print(f"Player {char} won the game!")
        break
    count+=1
else:
    print("It's a Draw!")
