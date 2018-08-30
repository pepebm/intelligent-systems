from queue import Queue
import pry

# 8 puzzle solver, implementation with BFS and DFS
# Made by: Jose Manuel Beauregard Mendez - 

# Node class that will represent a movement with it's parent step
class Node:
    route = ''
    zero = []

    def __init__(self, parent, zeroPosition, direction, move='X'):
        self.parent = parent
        self.move = move
        self.direction = direction
        self.zero = zeroPosition
    
    def makeMovement(self):
        pry()
        if self.move != 'X':
            self.current = _swap(self.zero, [self.move[0], self.move[1]], self.parent.current)
            if self.direction != '':
                self.route += self.parent.route + ('-' + self.direction + '-> ')

# main function
def busquedaNoInformada(edoInicial, edoFinal, algoritmo):
    result = ''
    if edoInicial == edoFinal:
        result = 'Already solved'
    else:
        if algoritmo == 0:
            result = bfsImplementation(edoInicial, edoFinal)
        else:
            dfsImplementation(edoInicial, edoFinal)
    return result

# Breadth-first search approach with a queue
def bfsImplementation(initial, end):
    # Initializing
    sol = 0
    cost = 0
    result = ''
    zero = _findZero(initial)
    # Add initial state manually
    nodes = [Node(initial, zero, '', zero)]
    nodes[0].current = initial
    nodes[0].route = ''
    nodes[0].parent = nodes[0]
    # Add current node position as visited
    visited = []
    # Loop until every possible solution is calculated,
    # if a solution is found, the cycle breaks
    while len(nodes) != 0:
        # FIFO
        node = nodes.pop(0)
        # Check if we have the solution
        if node.parent.current == end:
            sol = 1
            result = node.route
            break
        # Find the possible moves and make a Node for each one
        for m in _checkMove(node.zero, visited):
            # Build new branches of the tree
            nodes.append(Node(node, _findZero(node.parent.current), m.pop(), m))
        # Alter current node board before checking its new children node's
        node.makeMovement()
        print(node.route)
        # Add current node position, unless it's the first iteration
        visited.append([node.move[0], node.move[1]])
        # Add step
        cost += 1
    if sol != 1: result = 'No solution found'
    return result

# Depth-first search approach with a stack (Python list)
def dfsImplementation(current, end):
    initial = current
    zeroPosition = _findZero(current)
    firstSteps = _checkMove(zeroPosition, [zeroPosition], 1)
    sol = 0
    while not firstSteps.empty():
        # This array will have the visited positions
        visited = [zeroPosition]
        # Structure were we'll save the movements
        moves = []
        # Create all the possible ways to start
        moves.append(firstSteps.pop())
        # String were we'll save the final result, if any
        result = ''
        while not moves.empty():
            nextMove = moves.pop()
            _swap(zeroPosition, nextMove, current)
            visited.append([nextMove[0], nextMove[1]])
            result += ('-' + nextMove[2] + '-> ')
            print(result)
            print(current)
            print(moves.queue)
            # Check if we have the solution
            if current == end:
                sol = 1
                break
            # Get new position
            zeroPosition = _findZero(current)
            print(zeroPosition)
            # Find new movements, if none found and moves is empty, the while will end
            moves = moves + _checkMove(zeroPosition, visited)
        # Stop finding paths if solution is found
        if sol == 1: break
    if sol != 1: result = 'No solution found'
    return result

# Helper function that will return X & Y position of Zero
def _findZero(arr):
    for i in range(len(arr)):
        try:
            idx = arr[i].index(0)
            return [i, idx]
        # Expecting failure if index is not found
        except ValueError: pass

# Helper funcition that will check possible moves given the zero position
def _checkMove(zeroPosition, visited):
    print('v')
    print(visited)
    x = zeroPosition[0]
    y = zeroPosition[1]
    # This formula will create a sequential id for each position given their coordinates
    idx = (x * 3) + y
    #print('zero id: '+ str(idx))
    nextMoves = []
    # right
    if idx % 3 < 2:
        if not _checkVisited(visited, [x, y + 1]):
            nextMoves.append([x, y + 1, 'R'])
    # down
    if idx < 6:
        if not _checkVisited(visited, [x + 1, y]):
            nextMoves.append([x + 1, y, 'D'])
    # left
    if idx % 3 > 0:
        if not _checkVisited(visited, [x, y - 1]):
            nextMoves.append([x, y - 1, 'L'])
    # up
    if idx > 2:
        if not _checkVisited(visited, [x - 1, y]):
            nextMoves.append([x - 1, y, 'U'])
    return nextMoves


# Helper function that will check if the move has already been done
# return True if found
def _checkVisited(visited, move):
    result = False
    for pos in visited:
        if move == pos: 
            result = True
    return result

# Helper function to swap elements in the 2d list
def _swap(start, finish, arr):
    print('Move ' + str(start[0]) + str(start[1]) +
         ' to ' + str(finish[0]) + str(finish[1]))
    print('s')
    print(arr)
    newBoard = arr
    startX, startY = start[0], start[1]
    finishX, finishY = finish[0], finish[1]
    temp = newBoard[startX][startY]
    newBoard[startX][startY] = newBoard[finishX][finishY]
    newBoard[finishX][finishY] = temp
    print('f')
    print(newBoard)
    return newBoard
