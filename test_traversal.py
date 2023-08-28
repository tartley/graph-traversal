'''
Test of basic graph traversal algorithms.
Python 3.3
'''
import unittest

import traversal

# Copy the example network used in the description at 'Graph Traversals'
# https://www.youtube.com/watch?v=or9xlA3YYzo
#
#  b-----f--c--h
#  |\    |
#  | \   |
#  |  a--d
#  |  |
#  |  |
#  |  |
#  e--g

EDGES = [
    'ab',
    'ad',
    'ag',
    'be',
    'bf',
    'cf',
    'ch',
    'df',
    'eg',
]

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

class Test(unittest.TestCase):

    def test_nodes(self):
        self.assertEqual(
            nodes(EDGES),
            {
                'a': 'bdg',
                'b': 'aef',
                'c': 'fh',
                'd': 'af',
                'e': 'bg',
                'f': 'bcd',
                'g': 'ae',
                'h': 'c',
            }
        )

    def assert_depth_first(self, implimentation):
        self.assertEqual(
            list(implimentation(nodes(EDGES), 'a')),
            ['a', 'b', 'e', 'g', 'f', 'c', 'h', 'd']
        )

    def test_depth_first_recursive(self):
        self.assert_depth_first(traversal.depth_first_recursive)

    def test_depth_first_iterative(self):
        self.assert_depth_first(traversal.depth_first_iterative)

    def assert_breadth_first(self, implementation):
        self.assertEqual(
            list(implementation(nodes(EDGES), 'a')),
            ['a', 'b', 'd', 'g', 'e', 'f', 'c', 'h']
        )

    def test_breadth_first_iterative(self):
        self.assert_breadth_first(traversal.breadth_first_iterative)

if __name__ == '__main__':
    unittest.main()

