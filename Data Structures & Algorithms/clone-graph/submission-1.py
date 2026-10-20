"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodes: dict[int: Node] = {}

        def clone(node):
            copy = nodes.get(node.val)
            if not copy:
                copy = Node(node.val)
                nodes[node.val] = copy

                for nb in node.neighbors:
                    copy.neighbors.append(clone(nb))

            return copy

        copy = clone(node)
        return copy
        