'''
Basic graph traversal algorithms.

I like the way these generators separate the traversal of the tree from
whatever use it's being put to. For example, if we're searching for
particular nodes, then that logic isn't embedded here in our traversal code.

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

def depth_first_iterative(neighbours, start):
    '''
    Uses a list as a stack.
    Produces same output as recursive solution above.
    '''
    visited = set()
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            yield current
            visited.add(current)
            for neighbour in sorted(neighbours[current], reverse=True):
                stack.append(neighbour)

