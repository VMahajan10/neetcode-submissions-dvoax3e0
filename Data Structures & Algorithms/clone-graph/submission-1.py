"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = collections.deque()
        nodeToCopy = {}
        if not node:
            return None 
        x = Node(node.val)
        nodeToCopy[node] = x 
        q.append(node)

        while q:
            k = q.popleft()
            for nei in k.neighbors:
                if nei not in nodeToCopy:
                    r = Node(nei.val)
                    nodeToCopy[nei] = r 
                    q.append(nei)
                nodeToCopy[k].neighbors.append(nodeToCopy[nei])
        return nodeToCopy[node]


