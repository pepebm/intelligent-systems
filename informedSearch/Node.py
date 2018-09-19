# Node class that will represent a movement with it's parent step
class Node:
    def __init__(self, parent, zeroPosition, direction, generalCost, method, goal):
        self.parent = parent
        self.direction = direction
        self.zero = zeroPosition
        self.generalCost = generalCost
        self.route = ''
        self.goal = goal
        self.currentCost = 0
        if not isinstance(self.parent, list):
            self.makeMovement()
        else:
            self.current = self.parent
        if method is 0:
            self.countUnallocated()
        else:
            for i, a in enumerate(self.current):
                for j, b in enumerate(a):
                    self.currentCost += self.getDistance(b, i, j)

    # Function that will make the move based on the direction of the Node
    def makeMovement(self):
        self.current = self.swap(
            self.zero, self.calculateMove(), self.parent.current
        )
        # Validates non valid moves
        if (self.direction != '') or (self.current != self.parent.current):
            self.route += self.parent.route + ('-' + self.direction + '-> ')

    # Function that will return [x,y] position of the new move
    def calculateMove(self):
        zero = self.zero
        # Validates non valid moves
        if self.direction == '':
            newPos = zero
        else:
            if self.direction == 'R':
                newPos = [zero[0], zero[1] + 1]
            elif self.direction == 'D':
                newPos = [zero[0] + 1, zero[1]]
            elif self.direction == 'L':
                newPos = [zero[0], zero[1] - 1]
            elif self.direction == 'U':
                newPos = [zero[0] - 1, zero[1]]
        return newPos

    # Helper function to swap elements in the 2d list
    def swap(self, start, finish, arr):
        if (finish[0] < 0 or finish[0] > 2) or (finish[1] < 0 or finish[1] > 2):
            return arr
        newBoard = self.deepCopy(arr)
        startX, startY = start[0], start[1]
        finishX, finishY = finish[0], finish[1]
        temp = newBoard[startX][startY]
        newBoard[startX][startY] = newBoard[finishX][finishY]
        newBoard[finishX][finishY] = temp
        return newBoard

    # Helper function that will correctly copy the 8 puzzle board
    def deepCopy(self, arr):
        result = [[], [], []]
        for idx, item in enumerate(arr):
            result[idx] = item.copy()
        return result
    
    # Helper function that will count the number out of place
    def countUnallocated(self):
        counter = 0
        for i in range(len(self.current)):
            for j in range(len(self.current)):
                if self.current[i][j] != self.goal[i][j]:
                    counter += 1
        self.currentCost = counter

    # Helper function that will make the calcs of Manhanttan distance
    # for each position
    def getDistance(self, search, _x, _y):
        for i, a in enumerate(self.goal):
            try:
                y = a.index(search)
                x = i
                break
            except ValueError:
                pass
        return abs(y - _y) + abs(x - _x)        
