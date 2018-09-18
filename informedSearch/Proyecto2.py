from Node import Node

# 8 puzzle solver, implementation with A*
# where two heuristic's will be tested to complete f(n) = g(n) + h(n),
# the cost in each step will be calculated based on be Distance Manhattan 
# & number's out of place 
# Made by: Jose Manuel Beauregard Mendez - A01021716

# main function
def busquedaAstar(edoInicial, edoFinal, heuristica):
    result = ''
    if edoInicial == edoFinal:
        result = 'Already solved'
    else:
        if heuristica == 0:
            result = slots(edoInicial, edoFinal)
        else:
            result = projectManhattan(edoInicial, edoFinal)
    return result

# Distance Manhattan heuristic approach
def projectManhattan(initial, end):
    # Initializing
    sol = 0
    result = ''
    zero = _findZero(initial)
    # Add initial state manually
    nodes = [Node(initial, zero, '')]
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
        node.makeMovement()
        if not _checkVisited(visited, node):
            # Add new node position
            visited.append(node.current)
        else:
            # If node has already been visited skip this iteration
            continue
        # Check if we have the solution
        if node.current == end:
            sol = 1
            result = node.route
            break
        # Find the possible moves and make a Node for each one
        for m in _checkMove(node.zero, visited):
            # Build new branches of the tree
            nodes.append(Node(node, _findZero(node.current), m))
    if sol != 1:
        result = 'No solution found'
    return result

# Numbers out of place heuristic approach
def slots(initial, end):
    # Initializing
    sol = 0
    result = ''
    zero = _findZero(initial)
    # Add initial state manually
    nodes = [Node(initial, zero, '')]
    nodes[0].current = initial
    nodes[0].route = ''
    nodes[0].parent = nodes[0]
    # Add current node position as visited
    visited = []
    # Loop until every possible solution is calculated,
    # if a solution is found, the cycle breaks
    while len(nodes) != 0:
        # LIFO
        node = nodes.pop()
        node.makeMovement()
        if not _checkVisited(visited, node):
            # Add new node position
            visited.append(node.current)
        else:
            # If node has already been visited skip this iteration
            continue
        # Check if we have the solution
        if node.current == end:
            sol = 1
            result = node.route
            break
        # Find the possible moves and make a Node for each one
        for m in _checkMove(node.zero, visited):
            # Build new branches of the tree
            nodes.append(Node(node, _findZero(node.current), m))
    if sol != 1:
        result = 'No solution found'
    return result

# Helper function that will return X & Y position of Zero
def _findZero(arr):
    for i in range(len(arr)):
        try:
            idx = arr[i].index(0)
            return [i, idx]
        # Expecting failure if index is not found
        except ValueError:
            pass

# Helper funcition that will check possible moves given the zero position
def _checkMove(zeroPosition, visited):
    x = zeroPosition[0]
    y = zeroPosition[1]
    # This formula will create a sequential id for each position given their coordinates
    idx = (x * 3) + y
    nextMoves = []
    # down
    if idx < 6:
        nextMoves.append('D')
    # up
    if idx > 2:
        nextMoves.append('U')
    # left
    if idx % 3 > 0:
        nextMoves.append('L')
    # right
    if idx % 3 < 2:
        nextMoves.append('R')
    return nextMoves

# Helper function that will check if the move has already been done
# return True if found
def _checkVisited(visited, node):
    result = False
    for idx, item in enumerate(visited):
        if item == node.current:
            result = True
    return result

# Helper function that will print the 2d formatted in a 8 puzzle board
def _printMatrix(arr):
    for i in arr:
        print(i)
    print('')

def _countUnallocated(current, goal):
    counter = 0
    for i in range(len(current)):
        for j in range(len(current)):
            if current[i][j] != goal[i][j]:
                counter += 1
