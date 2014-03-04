'''
Test of basic graph traversal algorithms.
Python 3.3
'''
import unittest

from traversal import nodes

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

if __name__ == '__main__':
    unittest.main()
        
