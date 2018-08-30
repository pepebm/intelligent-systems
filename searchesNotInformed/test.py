from Proyecto1 import busquedaNoInformada

# edoInicial = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
# edoFinal = [[1, 3, 4], [8, 0, 5], [7, 2, 6]]

# edoInicial = [[1, 3, 4], [8, 6, 2], [0, 7, 5]]
# edoFinal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

edoInicial = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
edoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# edoInicial = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
# edoFinal = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
algoritmo = 1   # puede ser 0 para BFS o 1 para DFS
print(busquedaNoInformada(edoInicial, edoFinal, algoritmo))
