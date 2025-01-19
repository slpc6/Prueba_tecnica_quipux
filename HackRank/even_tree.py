"""
https://www.hackerrank.com/challenges/even-tree/problem
"""
#External lebraries
from collections import defaultdict


def evenForest(t_nodes: int, t_edges: int, t_from: list[int], t_to: list[int]) -> int:
    """Calcula la cantidad de arboles posibles con nodos pares

    args:
        t_nodes: el numero de nodos en el arbol
        t_edges: el numero de aristas indirectas en el arbol
        t_from: inicio del arbol por nodo
        t_to: nodo final por arista
    
    return:
        cantidad de arboles pares

"""
    arbol = defaultdict(list)
    for i, j in zip(t_from, t_to):
        arbol[i].append(j)
        arbol[j].append(i)

    sub_arbol = [0] * (t_nodes + 1)
    
    def dfs(node, parent):
        sub_arbol[node] = 1
        for neighbor in arbol[node]:
            if neighbor != parent:
                dfs(neighbor, node)
                sub_arbol[node] += sub_arbol[neighbor]
    dfs(1, -1)

    res = 0
    for i in range(2, t_nodes + 1):
        if sub_arbol[i] % 2 == 0:
            res += 1
    
    return res


if __name__ == '__main__':

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)
    print(res)
