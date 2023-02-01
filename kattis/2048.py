# Status: In Progress
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
    for i in range(4):
        column1, column2, column3, column4 = [0, 0, 0, 0]
        for j in range(4):
            pass


def right(gameBoard):
    pass

def down(gameBoard):
    pass


if __name__ == '__main__':
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    board = makeBoard(line1, line2, line3, line4)
    print(left(board))
