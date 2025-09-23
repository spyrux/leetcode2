"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #get outgoing adj list for each node
        #node val is unique for each node
        visited = set()
        if not node:
            return None
        queue = [node]
        node_map = {}

        while queue:
            curr = queue.pop(0)
            if curr.val not in node_map:
                node_map[curr.val] = Node(curr.val,[])
            for neighbor in curr.neighbors:
                if neighbor.val not in node_map:
                    node_map[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                node_map[curr.val].neighbors.append(node_map[neighbor.val])

        
        return node_map[node.val]




        