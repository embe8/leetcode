'''Neetcode: Valid Tree: Given a list of lists[int] and number of nodes n where the list are the edges, determine if the tree is valid 
where a valid tree has no cycles and the number of edges should be n - 1
Approach: Place the edges in an adjacency list, use a set to keep track of visisted nodes using bfs, and use a deque to keep track of nodes
to visit, at the end if the length of visited equals to node return True
IMPORTANT: uses breadth first search starting from node 0 and its parent (itself so -1)'''


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
        q = deque([(0, -1)]) #  (current node, previous node) -1 means it does not have a parent, 0 is the first node so no parent
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

# Same solution but with different comments ( more descriptive of each step )
class Solution:
    def validTree(self, n: int, edges: List[List[int]])->bool:
        # edge case
        if len(edges) > (n-1): return False
        # create adj list
        adj = [[] for _ in range(n + 1)]
        # create the edges, undirected so need to append both ways
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # create the set that will keep track of visited nodes
        visited = set()
        # use a deque to keep track of nodes to visit
        q = deque([(0, -1)])
        visited.add(0)

        while q:
            # while there are nodes to traverse
            node, parent = q.popleft() # remember (0, -1) is the first node and -1 because it has no parent so here we get node, parent
            # visit each node's neighbor
            for neighbor in adj[node]:
                if neighbor == parent: continue # skip already visited
                if neighbor in visited: return False # can't visist twice if valid tree

                visited.add(neighbor)
                q.append((neighbor, node))

        return len(visited) == n

'''
1. First initialize the adjacency list and handle edge case where number of edges is greater than (n - 1)
2. For adjacency list, append each u, v edge both ways u to v and v to u since it's undirected
3. Use a set to keep track of visited nodes and a deque to keep track of nodes to traverse
4. First node to be visited is 0 current node and -1 since it has no parent
5. Start bfs, 
'''



