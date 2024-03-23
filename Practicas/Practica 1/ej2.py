"""
a) (n^2)! ya que por cada casilla tiene n^2 opciones y despues (n^2 -1)
   y asi susesivamente hasta que nos quede 1 opcion.
b) mi idea para el algoritmo es ir asignando a random los cuadrados y al final verificar si
    es un cuadrado magico
c) en el peor caso es O((n^2)!) ya que cada nodo puede tener hasta (n^2 - i) hijos, donde i es la 
   cantidad de numeros ya asignados. mientras mas cerca de la raiz estemos mas ramificaciones hay.
   si sumamos todos los nodos el orden nos da (n^2)!
"""
#d) para mi algoritmo considero que el numero magico ya esta dado. c representa la lista de elementos a elejir
# nummag el numero magico a verificar y 


def cuadradoMagico(c : list, nummag : int, res, soluciones):
    return False 