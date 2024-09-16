import sys

def factorial(n: int) -> int: 
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Llamada recursiva
    else:
        return n * factorial(n - 1)

print('Factorial de: ', factorial(1000))
print(sys.getrecursionlimit())