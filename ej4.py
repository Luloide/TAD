import random
# me falta la poda tho
def RutaMinima(pi : list , n, matriz, res,  soluciones):
    if len(res) == n:
        # si no hay solucion hasta ahora agrega esa
        if soluciones == []:
            soluciones.append(res)
        elif (suma(res,n, matriz) <= suma(soluciones[0],n, matriz)):
            if (suma(res,n, matriz) < suma(soluciones[0],n, matriz)): # si encuentra una solucion mejor elimina las anteriores
                soluciones = []
                soluciones.append(res)
            else :
                soluciones.append(res) # si encuentra otra solucion igual, la agrega como valida
            return soluciones
    else:
        for i in range(len(pi)):
            #agarra un elem
            elem = pi[i]
            #elimina el elem de la lista
            picp = pi[:i] + pi[i+1:]
            # mira las demas permutaciones
            RutaMinima(picp, n, matriz, res + [elem], soluciones)
    return soluciones

def suma(posiblesol,n, matriz):
    res = matriz[n-1][0]
    for i in range(n-1):
        res += matriz[i][i+1]
    return res


matriz_ejemplo = [[0,1,10,10],[10,0,3,15],[21,17,0,2],[3,22,30,0]]
print(suma([1,2,3,4],4, matriz_ejemplo))
#print(RutaMinima([1,2,3,4], 4,matriz_ejemplo, [], []))