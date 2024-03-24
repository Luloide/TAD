import random
import copy
"""
a) (n^2)! ya que por cada casilla tiene n^2 opciones, despues (n^2 - 1)
   y asi susesivamente hasta que nos quede 1 opcion.
b) mi idea para el algoritmo es ir asignando a random los cuadrados y al final verificar si
    es un cuadrado magico
c) en el peor caso es O((n^2)!) ya que cada nodo puede tener hasta (n^2 - i) hijos, donde i es la 
   cantidad de numeros ya asignados. mientras mas cerca de la raiz estemos mas ramificaciones hay.
   si sumamos todos los nodos el orden nos da (n^2)!
"""
#d) para mi algoritmo considero que el numero magico ya esta dado. c representa la lista de elementos a elejir
# nummag el numero magico a verificar y 

def cuadradoMagico(c, n, nummag, res, soluciones, i=0, j=0):
    if i == n:
        if cuadradoValido(res, nummag):
            soluciones.append([fila[:] for fila in res])
        return soluciones

    for elem in c:
        c_copy = c[:]
        c_copy.remove(elem)
        res[i][j] = elem
        if sumaFila(res, i) <= nummag and sumaColumna(res, j) <= nummag:
            if j < n - 1:
                soluciones = cuadradoMagico(c_copy, n, nummag, copy.deepcopy(res), soluciones, i, j+1)
            elif i < n - 1:
                soluciones = cuadradoMagico(c_copy, n, nummag, copy.deepcopy(res), soluciones, i + 1, 0)
            else:
                if cuadradoValido(res, nummag):
                    soluciones.append([fila[:] for fila in res])
    return soluciones


def cuadradoValido(posres, numeroMagico):
    dimension = len(posres)
    diagonal_principal = sum(posres[i][i] for i in range(dimension))
    diagonal_secundaria = sum(posres[i][dimension - i - 1] for i in range(dimension))
    #chequea fila y columna
    for fila in posres:
        if sum(fila) != numeroMagico:
            return False
    for col in range(dimension):
        if sum(posres[fila][col] for fila in range(dimension)) != numeroMagico:
            return False
    #chequea diagonales
    if diagonal_principal != numeroMagico or diagonal_secundaria != numeroMagico:
        return False
    return True  


def sumaFila(matriz, fila):
    return sum(matriz[fila])

def sumaColumna(matriz, columna):
    return sum(matriz[fila][columna] for fila in range(len(matriz)))

def generar_matriz_vacia(n):
    matriz = []
    for _ in range(n):
        fila = [0] * n
        matriz.append(fila)
    return matriz

cuadrados_magicos = cuadradoMagico(list(range(1, 10)), 3, 15, generar_matriz_vacia(3), [], 0 ,0)
print(cuadrados_magicos)
