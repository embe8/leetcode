'''Problem: Find redundant connection, given a List of integer lists named 'edges' find if there's a redundant connection
and return the list of nodes (edge) that is redundant
Approach: Create adjacency list and traverse tree using dfs, keep track of visited nodes and recursive dfs will return True
if the edge has been traversed before, the function that first called the dfs will register True and return the redundant
edge as [u, v]
'''

# Time complexity: O(E* (V + E))
# Space complexity: O(V + E)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        def dfs(node, parent):
            if visited[node]: return True

            visited[node] = True
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    return True
            return False



        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            visited = [False] * (n + 1)

            if dfs(u, -1):
                return [u,v]
        return []

# Optimal solution
# Time complexity: O(V + E)
# Space complexity: O(V + E)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]])->List[int]:
        n = len(edges)
        # create the adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # keep track of visited nodes
        visited = [False] * (n+1)
        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True
            visited[node] = True
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        # first call to dfs
        dfs(1, -1) # 1 is the first node and its parent is itself
        # find the last nodes visited in the cycle
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []




        
