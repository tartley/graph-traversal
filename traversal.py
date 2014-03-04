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

