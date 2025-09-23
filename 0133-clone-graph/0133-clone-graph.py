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
        out_map = {}
        in_map = {}

        while queue:
            curr = queue.pop(0)
            #already visited this node
            if not curr or curr.val in node_map:
                continue
            else:
                node_map[curr.val] = Node(val = curr.val)
                for neighbor in curr.neighbors:
                    if neighbor.val in in_map:
                        in_map[neighbor.val].append(curr.val)
                    else:
                        in_map[neighbor.val] = [curr.val]
                    if neighbor.val not in node_map:    
                        queue.append(neighbor)
        
        print(node_map)
        for key, value in in_map.items():
            curr = key
            for edge in value:
                node_map[curr].neighbors.append(node_map[edge])
        
        return node_map[node.val]




        