"""
Dado el termino t1, t2 y n
el termino iesimo sera ti+2 = ti+(ti+1)^2
calcular el termino n
https://www.hackerrank.com/challenges/fibonacci-modified/problem
"""

def fibonacciModified(t1: int, t2: int, n: int) -> int:
    """Calcula la funcion de fibonacci modificada

    Args:
        t1 (int): primer termino
        t2 (int): segundo termino
        n (int): termino a calcular
    
    return:
        el numero n de la serie
    
    """
    if n == 1:
        return t1
    elif n == 2:
        return t2

    for _ in range(3, n + 1):
        t1, t2 = t2, t1 + t2**2
    return t2


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)
    print(result, sep='\n')