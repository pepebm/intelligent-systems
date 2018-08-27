from queue import Queue

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
    firstSteps = _checkMove(zeroPosition, [])
    code = 0
    while not firstSteps.empty():
        visited = []
        moves = Queue()
        moves.put(firstSteps.get())
        result = ''
        while not moves.empty():
            nextMove = moves.get()
            print(nextMove)
            current = _swap(zeroPosition, nextMove, current)
            visited.append(nextMove)
            result += ('- ' + nextMove[2] + ' ->')
            if current == end:
                code = 1
                break
            zeroPosition = _findZero(current)
            moves = _mergeQueues(moves, _checkMove(zeroPosition, visited))
        if code == 1: break
    if code != 1: result = 'No solution found'
    return result

# Depth-first search approach with a stack (Python list)
def dfsImplementation(current, end):
    stack = []

# Helper function that will return X & Y position of Zero
def _findZero(arr):
    for i in range(len(arr)):
        try:
            idx = arr[i].index(0)
            return [i, idx]
        # Expecting failure if index is not found
        except ValueError:
            pass

# Helper function to swap elements in the 2d list 
def _swap(start, finish, arr):
    startX, startY = start[0], start[1]
    finishX, finishY = finish[0], finish[1]
    temp = arr[startX][startY]
    arr[startX][startY] = arr[finishX][finishY]
    arr[finishX][finishY] = temp
    return arr

# Helper funcition that will check possible moves given the zero position
def _checkMove(zeroPosition, visited, algorithm = 0):
    if algorithm == 0:
        x = zeroPosition[0]
        y = zeroPosition[1]
        idx = (x * 3) + y
        nextMoves = Queue()
        # left
        print(idx)
        if idx % 3 > 0:
            if [x - 1, y] not in visited:
                nextMoves.put([x - 1, y, 'L'])
        # down
        if idx < 6:
            if [x, y + 1] not in visited:
                nextMoves.put([x, y + 1, 'D'])
        # right
        if idx % 3 < 2:
            if [x + 1, y] not in visited:
                nextMoves.put([x + 1, y, 'R'])
        # up
        if idx > 2:
            if [x, y - 1] not in visited:
                nextMoves.put([x, y - 1, 'U'])
    else:
        nextMoves = _checkMoveList(zeroPosition, visited)
    return nextMoves


def _checkMoveList(zeroPosition, visited):
    x = zeroPosition[0]
    y = zeroPosition[1]
    idx = (x * 3) + y
    nextMoves = []
    # left
    if idx % 3 > 0:
        if [x - 1, y] not in visited:
            nextMoves.append([x - 1, y, 'L'])
    # down
    if idx < 6:
        if [x, y + 1] not in visited:
            nextMoves.append([x, y + 1, 'D'])
    # right
    if idx % 3 < 2:
        if [x + 1, y] not in visited:
            nextMoves.append([x + 1, y, 'R'])
    # up
    if idx > 2:
        if [x, y - 1] not in visited:
            nextMoves.append([x, y - 1, 'U'])
    return nextMoves

# Helper function that will put b's values in a Queue
def _mergeQueues(a, b):
    while not b.empty():
        a.put(b.get())
    return a
