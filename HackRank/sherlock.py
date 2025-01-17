"""
Numero decente:
Sus dígitos solo pueden ser 3 y/o 5.
El número de dígitos 5 debe ser divisible por 3.
El número de dígitos 3 debe ser divisible por 5.
Entre todos los números que cumplen las condiciones, se elige el mayor posible.

https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
"""
def decentNumber(n: int) -> str:
    """Funcion para calcular el numero decente de longitud n
    Args:
        n: longitud del numero decente
    Returns:
        el numero decente de longitud n
    """
    for i in range(n + 1):
        if (n - i) % 3 == 0 and i % 5 == 0:
            print((n - i)*'5' + (i)*'3')
            return 
    print(-1)

if __name__ == '__main__':

    for t_itr in range(0, 101):
        decentNumber(t_itr)