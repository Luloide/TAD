import random
# ahora lo que estoy haciendo es intentar todos los subconjuntos de soluciones posibles
def maxiSubconjunto(pool, m, k, p, res, soluciones):
    if k == 0 or not pool:
        # esto lo que hace es no incluir ramas del largo < k
        if len(res) == p:
            # chequeo que la suma que genera sea la mas grande
            suma_actual = (suma(coordenadas(res), m))
            if (soluciones == []):
                soluciones.append(res)
                return soluciones
            else:
                suma_sol = suma(coordenadas(soluciones[0]), m)
            # en caso de ser mayor (no igual) que limpie las soluciones viejas
                if(suma_actual >= suma_sol):
                    if(suma_actual > suma_sol):
                        soluciones.clear()
                    soluciones.append(res)
                return soluciones
            
    else:
        elem = pool[0]
        poolcp = pool[1:]
        
        # Rama de incluir el elemento
        incluir = maxiSubconjunto(poolcp, m, (k - 1) , p, (res + [elem]), soluciones)
        
        # Rama de no incluir el elemento
        no_incluir = maxiSubconjunto(poolcp, m, k, p, res, soluciones)
        return incluir + no_incluir
    return [] 


def coordenadas(I):
    res = []
    for elem in I:
        resto = I[:]
        for item in resto:
            res.append((elem, item))
    return res

def suma(cord, matriz):
    suma = 0
    for tupla in cord:
        suma += matriz[tupla[0] - 1][tupla[1] - 1]
    return suma

print(maxiSubconjunto([1,2,3], [[2,7,6],[9,5,1],[4,3,8]],2,2,[],[]))                  