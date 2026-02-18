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
            
        
