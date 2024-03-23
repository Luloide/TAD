def subset_sum(c, i: int, j: int, res: list, soluciones):
    if j < 0: # si es menos de 0 se paso
        return False
    elif j == 0 and i == -1: # si evalua todos los elementos y llego a 0 es una solucion valida
        soluciones.append(res)
        return soluciones
    elif i == -1:
        return False
    else:
        result1 = subset_sum(c, i-1, j, res[:] + [0], soluciones)
        result2 = subset_sum(c, i-1, j - c[i], res[:] + [1], soluciones)
        if result1:
            return result1
        elif result2:
            return result2
        else:
            return False

print(subset_sum([6,12,6], 2, 12, [],[]))