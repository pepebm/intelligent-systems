"""
    Made by: José Manuel Beauregard Méndez - A0101716
    ---- Reversi with minimax ----
"""
from os import _exit
from copy import deepcopy
# TODO Delete this import at end
import pry

def validMove(board, x, y, player):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1: return False
    if board[y][x] != '0': return False
    boardTemp, num = createMove(deepcopy(board), x, y, player)
    if num == 0: return False
    return True

def bestMove(board, player):
    maxPoints, tempX, tempY = 0, -1, -1
    for y in range(n):
        for x in range(n):
            if validMove(board, x, y, player):
                boardTemp, num = createMove(deepcopy(board), x, y, player)
                points = minimax(boardTemp, player, depth, True)
                if points > maxPoints:
                    maxPoints = points
                    tempX = x
                    tempY = y
    return tempX, tempY

movesX = [-1, 0, 1, -1, 1, -1, 0, 1]
movesY = [-1, -1, -1, 0, 0, 1, 1, 1]
def createMove(board, x, y, player):
    # total number of opponent pieces taken
    totalNum = 0
    board[y][x] = player
    for i in range(n):
        num = 0
        for j in range(n):
            tempX, tempY = x + movesX[i] * (j + 1), y + movesY[i] * (j + 1)
            if tempX < 0 or tempX > n - 1 or tempY < 0 or tempY > n - 1:
                num = 0
                break
            elif board[tempY][tempX] == '0':
                num = 0
                break
            elif board[tempY][tempX] == player:
                break
            else:
                num += 1

        for j in range(num): board[x + movesX[i] * (j + 1)][y + movesY[i] * (j + 1)] = player
        totalNum += num
    return (board, totalNum)

def populateBoard():
    z = int((n - 2) / 2)
    board[z][z] = '2'
    board[n - 1 - z][z] = '1'
    board[z][n - 1 - z] = '1'
    board[n - 1 - z][n - 1 - z] = '2'

def printBoard():
    m = len(str(n - 1))
    for y in range(n):
        row = ''
        print(row + ' ' + str(y), end=' ')
        for x in range(n):
            row += board[y][x]
            row += ' ' * m
        print(row + ' ' + str(y))
    row = ''
    for x in range(1, n+1):
        row += str(x).zfill(m) + ' '
    print('   ' + row + '\n')

def boardValue(board, player):
    res = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == player:
                if (x == 0 or x == n - 1) and (y == 0 or y == n - 1): res += 4  # corner
                elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1): res += 2  # side
                else: res += 1
    return res

# if no valid move(s) possible then True
def pathEnd(board, player):
    for y in range(n):
        for x in range(n):
            if validMove(board, x, y, player): return False
    return True

def sortNodes(board, player):
    sortedNodes = []
    for y in range(n):
        for x in range(n):
            if validMove(board, x, y, player):
                boardTemp, totalNum = createMove(deepcopy(board), x, y, player)
                sortedNodes.append([boardTemp, boardValue(boardTemp, player)])
    sortedNodes = sorted(sortedNodes, key=lambda node: node[1], reverse=True)
    return [node[0] for node in sortedNodes]

def minimax(board, player, depth, minormax):
    if depth == 0 or pathEnd(board, player):
        return boardValue(board, player)
    # max
    if minormax:
        bestValue = -1
        for y in range(n):
            for x in range(n):
                if validMove(board, x, y, player):
                    boardTemp, totalNum = createMove(deepcopy(board), x, y, player)
                    bestValue = max(bestValue, minimax(boardTemp, player, depth - 1, False))
    # min
    else:
        bestValue = n * n + 4 * n + 4 + 1
        for y in range(n):
            for x in range(n):
                if validMove(board, x, y, player):
                    boardTemp, totalNum = createMove(deepcopy(board), x, y, player)
                    bestValue = min(bestValue, minimax(boardTemp, player, depth - 1, True))
    return bestValue

# Defaults
n = 8
depth = 4
board = [['0' for x in range(n)] for y in range(n)]

def othello(nivel, fichas, inicio):
    global depth
    global board
    depth = nivel
    print('Othello BOARD GAME with AI')
    populateBoard()
    turn = 0
    while True:
        turn += 1
        print('='*10, 'Round ' + str(turn), '='*10)
        for p in range(2):
            print()
            printBoard()
            player = str(p + 1)
            print('Human: ') if player == '1' else print('Computer: ')
            if pathEnd(board, player):
                print('No more valid moves\n\tFinal scores:')
                print('\t\P1: ' + str(boardValue(board, '1')))
                print('\t\tComputer: ' + str(boardValue(board, '2')))
                _exit(0)
            # User
            if player == '1':
                while True:
                    xy = input('X Y: ')
                    if xy == '': _exit(0)
                    try:
                        x, y = xy.split()
                    except ValueError:
                        print('*****Invalid input*****\n\tEnter X coordinate followed by a space and then Y coordinate')
                        continue
                    x, y = int(x), int(y)
                    if validMove(board, x, y, player):
                        board, totalNum = createMove(board, x, y, player)
                        print(str(totalNum), 'Piece(s) converted')
                        break
                    else:
                        print('Invalid move! Try again!')
            # Computer
            else:
                x, y = bestMove(board, player)
                if not (x == -1 and y == -1):
                    board, totalNum = createMove(board, x, y, player)
                    print('Computer moved (X Y): ' + str(x) + ' ' + str(y))
                    print(str(totalNum), 'Piece(s) converted')
