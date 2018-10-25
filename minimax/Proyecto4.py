"""
    Made by: José Manuel Beauregard Méndez - A01021716
    ---- Reversi Game with minimax ----
"""
from os import _exit
from copy import deepcopy

# Defaults
n = 8
# Char that represents empty (no move made in that spot) 
empty = '_'
# how deep we'll go
depth = 4
# 8x8 board filled with the char defined at empty
board = [[empty for x in range(n)] for y in range(n)]
# moves that will make the user, the index position is what we'll use
alphaMove = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# based on x & y, validate the move
def validMove(board, x, y, player):
    if isOnBoard(x, y): return False
    if board[y][x] != empty: return False
    boardTemp, num = createMove(deepcopy(board), x, y, player)
    if num == 0: return False
    return True

# Get the best move possible, this we'll be used by the computer
def bestMove(board, player):
    # starting values
    maxPoints, tempX, tempY = 0, -1, -1
    for y in range(n):
        for x in range(n):
            if validMove(board, x, y, player):
                # get all the possible moves
                boardTemp, num = createMove(deepcopy(board), x, y, player)
                points = minimax(boardTemp, player, depth, True)
                if points > maxPoints:
                    maxPoints = points
                    tempX = x
                    tempY = y
    return tempX, tempY

# Directions
movesX = [-1, 0, 1, -1, 1, -1, 0, 1]
movesY = [-1, -1, -1, 0, 0, 1, 1, 1]
def createMove(board, x, y, player):
    # total number of opponent pieces taken
    totalNum = 0
    # assume that the coordinates are valid ones, check after!
    board[y][x] = player
    # change board based on the new move
    for i in range(n):
        num = 0
        for j in range(n):
            tempX, tempY = x + movesX[i] * (j + 1), y + movesY[i] * (j + 1)
            if isOnBoard(tempX, tempY):
                num = 0
                break
            elif board[tempY][tempX] == empty:
                num = 0
                break
            elif board[tempY][tempX] == player:
                break
            else:
                num += 1
        # Change values that are enclosed by other player's move
        for j in range(num): board[y + movesY[i] * (j + 1)][x + movesX[i] * (j + 1)] = player
        totalNum += num
    return (board, totalNum)

# Populate board with init values, this never change
def initBoard():
    board[3][3] = 'B'
    board[3][4] = 'W'
    board[4][3] = 'W'
    board[4][4] = 'B'

# Print board nicely
def printBoard():
    m = len(str(n - 1))
    print('   ', end='')
    for i in alphaMove: print(i, end=' ')
    print()
    for y in range(1, n + 1):
        row = ''
        print(row, str(y), end=' ')
        for x in range(n):
            row += board[y - 1][x]
            row += ' ' * m
        print(row, str(y))
    print('   ', end='')
    for i in alphaMove: print(i, end=' ')
    print()

# Get score based on player
def boardValue(board, player):
    res = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == player:
                # corner
                if (x == 0 or x == n - 1) and (y == 0 or y == n - 1): res += 4
                # side
                elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1): res += 2
                else: res += 1
    return res

# Validate that position is in bound
def isOnBoard(x, y):
    return x < 0 or x > (n - 1) or y < 0 or y > (n - 1)

# checks if there's no more moves
def pathEnd(board, player):
    for y in range(n):
        for x in range(n):
            if validMove(board, x, y, player): return False
    return True

# sort moves based on player
def sortNodes(board, player):
    sortedNodes = []
    for y in range(n):
        for x in range(n):
            if validMove(board, x, y, player):
                boardTemp, totalNum = createMove(deepcopy(board), x, y, player)
                sortedNodes.append([boardTemp, boardValue(boardTemp, player)])
    return [node[0] for node in sorted(sortedNodes, key=lambda node: node[1], reverse=True)]

# the actual minimax appens here, this is used to calculate the best move possible
# from the computer
def minimax(board, player, depth, minormax):
    if depth == 0 or pathEnd(board, player): return boardValue(board, player)
    # max
    if minormax:
        for y in range(n):
            for x in range(n):
                if validMove(board, x, y, player):
                    boardTemp, totalNum = createMove(deepcopy(board), x, y, player)
                    bestValue = max(-1, minimax(boardTemp, player, depth - 1, False))
    # min
    else:
        for y in range(n):
            for x in range(n):
                if validMove(board, x, y, player):
                    boardTemp, totalNum = createMove(deepcopy(board), x, y, player)
                    bestValue = min(n * n + 4 * n + 4 + 1, minimax(boardTemp, player, depth - 1, True))
    return bestValue

# Params:
# nivel: 1 o 2
# fichas: 0 computadora juega blancas, 1 computadora juega negras
# inicio: 0 inicia la computadora, 1 inicia el jugador
def othello(nivel = 1, fichas = 1, inicio = 1):
    global depth
    global board
    depth = nivel
    print('Othello BOARD GAME with AI')
    initBoard()
    if fichas == 1: computer, p = 'B', 'W'
    else: computer, p = 'W', 'B'
    if inicio == 0: order = [computer, p]
    else: order = [p, computer]
    turn = 0
    while True:
        turn += 1
        print('='*10, 'Round', str(turn), '='*10)
        print('\tHuman:', str(boardValue(board, p)))
        print('\tComputer:', str(boardValue(board, computer)))
        for player in order:
            print()
            printBoard()
            print('Human:', '({})'.format(p)) if player == p else print('Computer: ')
            if pathEnd(board, player):
                print('No more moves', 'Final scores:', sep='\n')
                print('\tP1:', str(boardValue(board, p)))
                print('\tComputer:', str(boardValue(board, computer)))
                _exit(0)
            # User
            if player == p:
                while True:
                    userMove = input('X Y: ')
                    if userMove == '': _exit(0)
                    try:
                        x, y = userMove.split()
                        x, y = alphaMove.index(x.upper()), int(y) - 1
                    except ValueError:
                        print('***** Invalid input *****\n\tEnter X coordinate followed by a space and then Y coordinate')
                        continue
                    if validMove(board, x, y, player):
                        board, totalNum = createMove(board, x, y, player)
                        print(str(totalNum), 'Piece(s) converted')
                        break
                    else:
                        print('Error: Invalid move! Try again!')
            # Computer
            else:
                x, y = bestMove(board, player)
                if (x is not -1) and (y is not -1):
                    board, totalNum = createMove(board, x, y, player)
                    print('Computer moved (X Y):', alphaMove[x],  str(y + 1))
                    print(str(totalNum), 'Piece(s) converted')
