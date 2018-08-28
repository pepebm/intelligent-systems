from queue import Queue
import code
#code.interact(local=dict(globals(), **locals()))

# 8 puzzle solver, implementation with BFS and DFS
# Made by: Jose Manuel Beauregard Mendez - A01021716


# main function
def busquedaNoInformada(edoInicial, edoFinal, algoritmo):
    result = ''
    if algoritmo == 0:
        result = bfsImplementation(edoInicial, edoFinal)
    else:
        dfsImplementation(edoInicial, edoFinal)
    return result

# Breadth-first search approach with a queue
def bfsImplementation(current, end):
    initial = current
    zeroPosition = _findZero(current)
    firstSteps = _checkMove(zeroPosition, [zeroPosition])
    sol = 0
    while not firstSteps.empty():
        # This array will have the visited positions
        visited = [zeroPosition]
        # Structure were we'll save the movements
        moves = Queue()
        # Create all the possible ways to start
        moves.put(firstSteps.get())
        # String were we'll save the final result, if any
        result = ''
        while not moves.empty():
            nextMove = moves.get()
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
            moves = _mergeQueues(moves, _checkMove(zeroPosition, visited))
        # Stop finding paths if solution is found
        if sol == 1: break
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
            moves = moves + _checkMove(zeroPosition, visited, 1)
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

# Helper function to swap elements in the 2d list 
def _swap(start, finish, arr):
    print('Move ' + str(start[0]) + str(start[1]) +
          ' to ' + str(finish[0]) + str(finish[1]))
    startX, startY = start[0], start[1]
    finishX, finishY = finish[0], finish[1]
    temp = arr[startX][startY]
    arr[startX][startY] = arr[finishX][finishY]
    arr[finishX][finishY] = temp

# Helper funcition that will check possible moves given the zero position
def _checkMove(zeroPosition, visited, algorithm = 0):
    # If you need of a list instead of a Queue, put the third param to 1
    if algorithm == 0:
        x = zeroPosition[0]
        y = zeroPosition[1]
        # This formula will create a sequential id for each position given their coordinates
        idx = (x * 3) + y
        nextMoves = Queue()
        # right
        if idx % 3 < 2:
            if not _checkVisited(visited, [x, y + 1]):
                nextMoves.put([x, y + 1, 'R'])
        # down
        if idx < 6:
            if not _checkVisited(visited, [x + 1, y]):
                nextMoves.put([x + 1, y, 'D'])
        # left
        if idx % 3 > 0:
            if not _checkVisited(visited, [x, y - 1]):
                nextMoves.put([x, y - 1, 'L'])
        # up
        if idx > 2:
            if not _checkVisited(visited, [x - 1, y]):
                nextMoves.put([x - 1, y, 'U'])
    else:
        nextMoves = _checkMoveList(zeroPosition, visited)
    return nextMoves

# Helper function that will check possible moves and save them in a list
def _checkMoveList(zeroPosition, visited):
    x = zeroPosition[0]
    y = zeroPosition[1]
    # This formula will create a sequential id for each position given their coordinates
    idx = (x * 3) + y
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

# Helper function that will put b's values in a Queue
def _mergeQueues(a, b):
    while not b.empty(): a.put(b.get())
    return a

# Helper function that will check if the move has already been done
def _checkVisited(visited, move):
    result = False
    for pos in visited: if move == pos: result = True
    return result
