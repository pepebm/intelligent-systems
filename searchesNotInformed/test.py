from Proyecto1 import busquedaNoInformada
edoInicial = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
edoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
algoritmo = 0   # donde X puede ser 0 para BFS o 1 para DFS
print(busquedaNoInformada(edoInicial, edoFinal, algoritmo))
