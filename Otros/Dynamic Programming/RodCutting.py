""" 
el el capitulo 15 del libro de "Introduction to algorithims" en la seccion 15.1 presentan este problema,
mi idea es codearlo en la compu asi entiendo mas el aproach de dp.
El framework que encontre para resolver este tipo de problemas es el siguiente (Este framework lo explica 
Andrey Grehov en su curso sobre Dynamic Programming)
1. define the objective function
2. Identify base cases
3. write down a recurrance relation for the optimized objective funtion.
4. whats teh order of execution?
5. where to look for the answer?

aplicando este framework al problema:
1. f(i) es el valor del iesimo corte que da mas profit 
2. f(0) = 0 # ya que un rod que no puedo cortar no tiene beneficio
3. f(n) = max{p[n], f(n-1)}
4. bottom up
5. en r[n]
"""

def cutrod(n, p):
    r = [None] * (n+1)
    r[0] = 0
    i = 1
    while i <= n:
        r[i] = max(p[i], r[i-1])
        i = i+1
    return r[n]

prices = [1,5,8,9,10,17,17,20,24,30]
print(cutrod(4,prices))