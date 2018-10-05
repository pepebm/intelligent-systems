"""
    Made by: José Manuel Beauregard Méndez - A0101716
    ---- N - Queen problem with Hill Climbing ----
        · Heuristic: number of queens in attack position
"""
from random import randint
from numpy import zeros
from copy import deepcopy

def busquedaHC(N, lateral, M):
    for reps in range(M+1):
        board = createBoard(N)
        visited = []
        val = heuristic(board)
        qPos = findQueens(board)
        bestVal = board
        visitedBreak = False
        while val > 0 and not visitedBreak:
            v = 0
            for neighbor in qPos:
                moves = searchMoves(N, neighbor)
                for m in moves:
                    temp = generateMove(neighbor, m, board, N)
                    if checkVisited(visited, temp):
                        v += 1
                        if visitedBreak >= N:
                            visitedBreak = True
                            break
                        else: continue
                    neighborVal = heuristic(temp)
                    if neighborVal == 0:
                        bestVal = temp
                        print("*"*10, " Solution found in round {} ".format(reps), "*"*10)
                        printBoard(bestVal)
                        return
                    if neighborVal < val or (neighborVal <= val and lateral):
                        bestVal = temp
                        val = neighborVal
                    if qPos.index(neighbor) == len(qPos) - 1:
                        visitedBreak = True
                        break
                visited.append(temp)
            board = bestVal
            qPos = findQueens(board)
    print("No solution found in {} rounds".format(reps))

# This function will count the number of queens that are in
# attack position, that number will be the heuristic value
# that will determine the next action
def heuristic(b):
    h = 0
    qPos = findQueens(b)
    for i in range(len(qPos)):
        cQueen = qPos.pop(0)
        for j in range(len(qPos)):
            # Check row
            if(qPos[j][0] == cQueen[0]):
                h += 1
            # Check column
            if(qPos[j][1] == cQueen[1]):
                h += 1
            # Check diagonally
            if(abs(cQueen[0] - qPos[j][0]) == abs(cQueen[1] - qPos[j][1])):
                h += 1
    return h

# Helper function that will make a deepCopy of the current board &
# create a new one with the move passed
def generateMove(start, finish, b, N):
    new_b = deepcopy(b)
    new_b[start[0]][start[1]], new_b[finish[0]][finish[1]] = 0, 1
    return new_b

# Helper function that will check if current board has been visited previously
def checkVisited(visited, b):
    for i, item in enumerate(visited): 
        if(item == b): return True
    return False

# Helper function that will return the possible moves of a given Queen
def searchMoves(N, pos):
    moves = []
    # UP
    if (pos[0] - 1 >= 0): moves.append([pos[0]-1, pos[1]])
    # Down
    elif (pos[0] + 1 <= N - 1): moves.append([pos[0]+1, pos[1]])
    return moves

# Helper function that will return a list of list's with the different
# Queens position
def findQueens(b):
    pos = []
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j] == 1: 
                pos.append([i, j])
    return pos

# Helper function that will return a Board with randomly calculated Queens
def createBoard(N):
    b = [[0] * N for i in range(N)]
    for i in range(N): b[randint(0, N - 1)][i] = 1
    return b

# Helper function that will print the board passed
def printBoard(b):
    for i in b: print(i)
    print(' ')