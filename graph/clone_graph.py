"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None 
        
        mapList = {} # create a map
        mapList[node] = Node(node.val) # get value of first node and put in map
        q = deque([node]) # append node to queue to process

        while q:
            cur = q.popleft()
            for nei in cur.neighbors: # traverse neighbors of current node
                if nei not in mapList: # if it'ts not been explored
                    mapList[nei] = Node(nei.val) # place it in map
                    q.append(nei)
                # connect cloned current to cloned neighbor
                # get cloned current and append the cloned neighbors to it
                mapList[cur].neighbors.append(mapList[nei])

        return mapList[node]
        
