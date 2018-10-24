from Proyecto2 import busquedaAstar
edoInicial = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
edoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# 0 = numeros fuera de lugar
# 1 = distancia manhattan
heuristica = 1
print(busquedaAstar(edoInicial, edoFinal, heuristica))
