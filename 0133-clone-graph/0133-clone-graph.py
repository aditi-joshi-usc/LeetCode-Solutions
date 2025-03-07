"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def dfs(self, node, track):
        if node is None:
            return
        if node in track:
            return track[node]
        
        track[node] = Node(node.val, None)

        for neighbor in node.neighbors:
            if neighbor in track:
                track[node].neighbors.append(track[neighbor])
            else:
                self.dfs(neighbor, track)
                track[node].neighbors.append(track[neighbor])


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        track = {}
        if node is None:
            return None
        self.dfs(node, track)
        return track[node]
        