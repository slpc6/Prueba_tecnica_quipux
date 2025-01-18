"""
t_nodes: el numero de nodos en el arbol
t_edges: el numero de aristas indirectas en el arbol
t_from: inicio del arbol por nodo
t_to: nodo final por arista, (Match by index to t_from.)
https://www.hackerrank.com/challenges/even-tree/problem
10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
"""

def dfs(graph: dict, node: int, parent: int) -> int:
    """def: deep-first search

    args:
        graph: diccionario de nodos y aristas
        node: nodo actual
        parent: nodo padre
    
    return:
        int: cantidad de nodos pares
"""
    children = 0
    for child in graph[node]:
        if child != parent:
            children += dfs(graph, child, node)
    if children % 2 == 0:
        return 1
    return children + 1


def evenForest(t_nodes: int, t_edges: int, t_form: list[int], t_to: list[int]) -> int:
    """Calcula la cantidad de arboles posibles con nodos pares

    args:
        t_nodes: el numero de nodos en el arbol
        t_edges: el numero de aristas indirectas en el arbol
        t_from: inicio del arbol por nodo
        t_to: nodo final por arista
    
    return:
        cantidad de arboles pares

"""
    graph = {}
    for i in range(t_edges):
        if t_form[i] not in graph:
            graph[t_form[i]] = []
        if t_to[i] not in graph:
            graph[t_to[i]] = []
        graph[t_form[i]].append(t_to[i])
        graph[t_to[i]].append(t_form[i])

    return dfs(graph, 1, 0) - 1


if __name__ == '__main__':

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)
    print(res)
