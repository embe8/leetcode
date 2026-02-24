'''Neetcode: Valid Tree: Given a list of lists[int] and number of nodes n where the list are the edges, determine if the tree is valid 
where a valid tree has no cycles and the number of edges should be n - 1
Approach: Place the edges in an adjacency list, use a set to keep track of visisted nodes using bfs, and use a deque to keep track of nodes
to visit, at the end if the length of visited equals to node return True'''

# Space complexity: O(V + E)
# Time complexity: O(V + E)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]):
        # edge case if number of edges is more than n - 1
        if len(edges) > n - 1 : return False
        # create the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges: #   since undirected graph, need to append the nodes both ways
            adj[u].append(v)
            adj[v].append(u)
        visited = set() #   use set so duplicates are not included
        q = deque([(0, -1)]) #  (current node, previous node)
        visited.add(0) # 0 is the first node
        while q:
            node, parent = q.popleft()
            for neighbor in adj[node]:
                if neighbor == parent: continue

                if neighbor in visited: # an  edge can't be visited twice for a valid tree
                    return False

                visited.add(neighbor)
                q.append((neighbor, node))
        return len(visited) == n # if the number of nodes visited is equal to the number of nodes passed as argument, then it's a valid tree
