from random import randint, seed
from copy import deepcopy

def busquedaHC(N, lateral, M):
    seed(1)
    if lateral:
        print(sideMoveEnabled(N, M))
    else:
        print(sideMoveDisabled(N, M))

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
                continue
            # Check column
            if(qPos[j][1] == cQueen[1]):
                h += 1
                continue
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
                continue
            # Check column
            if(qPos[j][1] == cQueen[1]):
                h += 1
                continue
            # Check diagonally
            if(abs(cQueen[0] - qPos[j][0]) == abs(cQueen[1] - qPos[j][1])):
                h += 1
                continue
    return h

# Hill climbing algorithm without diagonal move's
def sideMoveDisabled(N, M):
    board = createBoard(N)
    visited = []
    val = heuristic(board)
    qPos = findQueens(board)
    bestVal = board
    while(val != 0):
        print('*'*15,' Round - ', M, ' ', '*'*15)
        M -= 1
        if not M >= 0:
            bestVal = 'No solution found'
            break
        for i in range(len(qPos)):
            neighbor = qPos.pop(0)
            moves = searchMoves(N, neighbor)
            for j in range(len(moves)):
                tempBoard = generateMove(neighbor, moves[j], board)
                if(checkVisited(visited, tempBoard)): continue
                neighborVal = heuristic(board)
                if(neighborVal < val):
                    bestVal = tempBoard
                    val = neighborVal
            visited.append(tempBoard)
        board = bestVal
        qPos = findQueens(board)
    return bestVal

# Hill climbing algorithm with diagonal move's
def sideMoveEnabled(N, M):
    board = createBoard(N)
    visited = []
    val = heuristic_Diagonal(board)
    qPos = findQueens(board)
    bestVal = board
    while(val != 0):
        print('*'*5,' Round - ', val, '*'*5)
        for i in range(len(qPos)):
            neighbor = qPos.pop(0)
            moves = searchMoves(N, neighbor)
            for j in range(len(moves)):
                tempBoard = generateMove(neighbor, moves[j], board)
                if(checkVisited(visited, tempBoard)): continue
                neighborVal = heuristic_Diagonal(board)
                if(neighborVal < val):
                    bestVal = tempBoard
                    val = neighborVal
            visited.append(tempBoard)
        board = bestVal
        qPos = findQueens(board)
    return bestVal

# Helper function that will make a deepCopy of the current board &
# create a new one with the move passed
def generateMove(start, finish, b):
    print("old board")
    printBoard(b)
    new_b = deepcopy(b)
    new_b[start[0]][start[1]], new_b[finish[0]][finish[1]] = 0, 1
    print("new board")
    printBoard(new_b)
    return new_b

# Helper function that will check if current board has been visited previously
def checkVisited(visited, b):
    result = False
    for i in range(len(visited)): 
        if(visited[i] == b): result = True
    return result

# Helper function that will return the possible moves of a given Queen
def searchMoves(N, pos):
    print(pos)
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
    for i in range(N): b[randint(0, N)][i] = 1
    return b

# Helper function that will print the board passed
def printBoard(b):
    for i in b: print(i)
    print(' ')

