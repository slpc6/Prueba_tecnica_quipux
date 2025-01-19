"""
https://www.hackerrank.com/challenges/strange-code/problem
"""


def strangeCounter(t: int) -> int:
    """Funcion para calcular el valor del contador en el tiempo t
    Args:
        t: valor de entrada que se quiere calcular
    Returns:
        el numero entero que representa el valor para el tiempo t en el contador
"""
    num = 3
    while t > num:
        t -= num
        num *= 2
    return num - t + 1
