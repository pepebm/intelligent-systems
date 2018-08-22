from Queue import Queue

def busquedaNoInformada(edoInicial, edoFinal, algoritmo):
    result = ''
    if algoritmo == 0:
        result = bfsImplementation(edoInicial, edoFinal)
    else:
        result = dfsImplementation(edoInicial, edoFinal)
    return result

def bfsImplementation(start, end):
    queue = Queue()

def dfsImplementation(start, end):
    stack = []

