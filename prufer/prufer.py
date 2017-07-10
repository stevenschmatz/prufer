'''
prufer.py - Prüfer sequence-to-tree conversion tools

Author: @stevenschmatz
'''

from typing import Tuple, List

Parent, Child = int, int
Edge = Tuple[Parent, Child]
Tree = List[Edge]

def build_tree(arr: List[int]) -> Tree:
    '''Converts a Prüfer sequence to its respective tree.'''

    if any([index > len(arr) for index in arr]):
        raise ValueError('All elements must be less than the length of the list.')

    tree = []

    graph = list(range(len(arr) + 2))
    degrees = [1] * len(graph)

    for node_index in arr:
        degrees[node_index] += 1

    for node_i in arr:
        for node_j in graph:
            if degrees[node_j] == 1:
                tree.append((node_i, node_j))
                degrees[node_i] -= 1
                degrees[node_j] -= 1
                break

    last = [index for index, val in enumerate(degrees) if val == 1]
    tree.append(tuple(reversed(last)))

    return tree
