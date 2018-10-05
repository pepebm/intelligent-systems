"""
    Made by: José Manuel Beauregard Méndez - A0101716
    ---- N - Queen problem with Hill Climbing ----
        · Heuristic: number of queens in attack position
"""

from random import randint
from copy import deepcopy

# TODO DELETE THIS IMPORT
import pry

def busquedaHC(N, lateral, M):
    if lateral:
        sideMoveEnabled(N, M)
    else:
        sideMoveDisabled(N, M)

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
    print("h: ", h)
    printBoard(b)
    return h

# This function will count the number of queens that are in
# attack position, that number will be the heuristic value
# that will determine the next action. This func will check diagonally
def heuristic_Diagonal(b):
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
    print("h: ", h)
    printBoard(b)
    return h

# Hill climbing algorithm without diagonal move's
def sideMoveDisabled(N, M):
    for reps in range(M):
        print('*'*15,' Round - ', reps, ' ', '*'*15)
        board = createBoard(N)
        visited = []
        val = heuristic(board)
        qPos = findQueens(board)
        bestVal = board
        while(val != 0):
            for i in range(len(qPos)):
                neighbor = qPos.pop(0)
                moves = searchMoves(N, neighbor)
                for j in range(len(moves)):
                    tempBoard = generateMove(neighbor, moves[j], board)
                    if checkVisited(visited, tempBoard): continue
                    neighborVal = heuristic(tempBoard)
                    if neighborVal == 0:
                        bestVal = tempBoard
                        printBoard(tempBoard)
                        return
                    if neighborVal < val:
                        bestVal = tempBoard
                        val = neighborVal
                visited.append(tempBoard)
            board = bestVal
            qPos = findQueens(board)
    print('No solution found')

# Hill climbing algorithm with diagonal move's
def sideMoveEnabled(N, M):
    for reps in range(M):
        print('*'*15,' Round - ', reps, ' ', '*'*15)
        board = createBoard(N)
        visited = []
        val = heuristic_Diagonal(board)
        qPos = findQueens(board)
        bestVal = board
        while(val != 0):
            for i in range(len(qPos)):
                neighbor = qPos.pop(0)
                moves = searchMoves(N, neighbor)
                for j in range(len(moves)):
                    tempBoard = generateMove(neighbor, moves[j], board)
                    if checkVisited(visited, tempBoard): continue
                    neighborVal = heuristic_Diagonal(tempBoard)
                    if neighborVal == 0:
                        bestVal = tempBoard
                        printBoard(tempBoard)
                        return
                    if neighborVal < val:
                        bestVal = tempBoard
                        val = neighborVal
                visited.append(tempBoard)
            board = bestVal
            qPos = findQueens(board)
    print('No solution found')

# Helper function that will make a deepCopy of the current board &
# create a new one with the move passed
def generateMove(start, finish, b):
    # print("old board")
    # printBoard(b)
    new_b = deepcopy(b)
    new_b[start[0]][start[1]], new_b[finish[0]][finish[1]] = 0, 1
    # print("new board")
    # printBoard(new_b)
    return new_b

# Helper function that will check if current board has been visited previously
def checkVisited(visited, b):
    result = False
    for i, item in enumerate(visited): 
        if(item == b): 
            result = True
    return result

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
    #pry()
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

