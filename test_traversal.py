'''
Test of basic graph traversal algorithms.
Python 3.3
'''
import unittest

from traversal import (
    breadth_first_iterative, depth_first_iterative, depth_first_recursive,
    nodes
)

# Copy the example network used in the description at 'Graph Traversals'
# https://www.youtube.com/watch?v=or9xlA3YYzo
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
        self.assert_depth_first(depth_first_recursive)

    def test_depth_first_iterative(self):
        self.assert_depth_first(depth_first_iterative)

    def test_breadth_first_iterative(self):
        self.assertEqual(
            list(breadth_first_iterative(nodes(EDGES), 'a')),
            ['a', 'b', 'd', 'g', 'e', 'f', 'c', 'h']
        )

if __name__ == '__main__':
    unittest.main()
        
