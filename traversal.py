'''
Basic graph traversal algorithms.
Python 3.3
'''

def nodes(edges):
    '''
    Utility function used to create a graph (dict of node: neighbours)
    from a sequence of edges, where:
        a node is represented by a single character identifier,
        an edge is a two character string,
        neighbours is a zero-or-more character string.
    '''
    edges = list(map(set, edges))
    nodes = set().union(*edges)
    return {
        node: ''.join(sorted(set().union(*(
            edge - set(node)
            for edge in edges
            if node in edge
        ))))
        for node in nodes
    }

def depth_first_recursive(neighbours, start, visited=None):
    '''
    Simplest looking algorithm, because it uses the call stack implicitly,
    rather than maintaining it explicitly like the iterative solution
    below. But call stacks area generally of limited size, e.g. CPython's
    defaults to 1,000 (see sys.getrecursionlimit)
    '''
    if visited is None:
        visited = set()
    yield start
    visited.add(start)
    for neighbour in neighbours[start]:
        if neighbour not in visited:
            yield from depth_first_recursive(neighbours, neighbour, visited)

