from queue import Queue

def busquedaNoInformada(edoInicial, edoFinal, algoritmo):
    result = ''
    if algoritmo == 0:
        bfsImplementation(edoInicial, edoFinal)
    else:
        dfsImplementation(edoInicial, edoFinal)
    return result

def bfsImplementation(current, end):
    q = Queue()
    zeroPosition = _findZero(current)
    #while current != end:

def dfsImplementation(current, end):
    stack = []


def _findZero(arr):
    for i in range(len(arr)):
        try:
            idx = arr[i].index(0)
            return [i, idx]
        except ValueError:
            pass

def _swap(startX, startY, finishX, finishY, arr):
    temp = arr[startX][startY]
    arr[startX][startY] = arr[finishX][finishY]
    arr[finishX][finishY] = temp
