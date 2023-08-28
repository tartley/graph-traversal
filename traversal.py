'''
Basic graph traversal algorithms.

I like the way these generators separate the traversal of the tree from
whatever use it's being put to. For example, if we're searching for
particular nodes, then that logic isn't embedded here in our traversal code.

Python 3.3
'''
from collections import deque

def depth_first_recursive(neighbours, start, visited=None):
    '''
    Simplest looking algorithm, because it uses the call stack implicitly,
    rather than maintaining it explicitly like the iterative solution
    below. But call stacks are sometimes of a limited size, e.g. CPython's
    defaults to 1,000 (see sys.getrecursionlimit), with no tail recursion.
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

def breadth_first_iterative(neighbours, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        current = queue.popleft()
        yield current
        for neighbour in sorted(neighbours[current]):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Breadth-first recursive is a fundamental mismatch. Breadth-first is most
# easily implemented using a queue, while doing it recursively implies using a
# (call) stack, which is the opposite of a queue. It can be done, but
# essentially by either implementing depth first and then re-ordering output to
# be breadth first, or by passing an entirely separate queue along the mostly
# redundant call stack.

