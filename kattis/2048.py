# Status: Complete
# https://open.kattis.com/problems/2048
# Takes the first 4 lines of input and returns a 2D array representing the 2048 board
def makeBoard(line1, line2, line3, line4):
    # Turns them into lists
    list1 = line1.split()
    list2 = line2.split()
    list3 = line3.split()
    list4 = line4.split()
    # Makes each number into actual ints
    for i in range(4):
        list1[i] = int(list1[i])
        list2[i] = int(list2[i])
        list3[i] = int(list3[i])
        list4[i] = int(list4[i])
    return [list1, list2, list3, list4]

# Idea is to move as much as possible then compile, doing it by only columns/rows at a time
def move(numList):
    for i in range(1,4):
        if (numList[i - 1] == 0):
            numList[i - 1] = numList[i]
            numList[i] = 0
    return numList

def compile(numList):
    for i in range(3):
        move(numList)
        move(numList)
        move(numList)
        move(numList)
        if numList[i] == numList[i + 1] and numList[i] != 0:
            numList[i] *= 2
            numList[i + 1] = 0
            numList = move(numList)
    return numList


def left(gameBoard):
    boardCopy = gameBoard
    for i in range(4):
        gameBoard[i] = compile(gameBoard[i])
    return boardCopy

def up(gameBoard):
    boardCopy = gameBoard
    for i in range(4):
        column = [0, 0, 0, 0]
        for j in range(4):
            column[j] = boardCopy[j][i]
        column = compile(column)
        for j in range(4):
            boardCopy[j][i] = column[j]
    return boardCopy

def right(gameBoard):
    boardCopy = gameBoard
    for i in range(4):
        # Reverses to compile then reverses again to get it in the right order
      temp = boardCopy[i]
      temp.reverse()
      temp = compile(temp)
      temp.reverse()
      boardCopy[i] = temp
    return boardCopy

def down(gameBoard):
    boardCopy = gameBoard
    for i in range(4):
        column = [0, 0, 0, 0]
        for j in range(4):
            column[j] = boardCopy[j][i]
        column.reverse()  
        column = compile(column)
        for j in range(4):
            boardCopy[3 - j][i] = column[j]
    return boardCopy

def printBoard(gameBoard):
    for row in gameBoard:
        print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))

if __name__ == '__main__':
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    board = makeBoard(line1, line2, line3, line4)
    direction = int(input())
    if direction == 0:
        printBoard(left(board))
    if direction == 1:
        printBoard(up(board))
    if direction == 2:
        printBoard(right(board))
    if direction == 3:
        printBoard(down(board))