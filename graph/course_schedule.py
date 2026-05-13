# Problem: Given a number of courses and prerequisites, check if all courses can be finished
# Approach: courses are the nodes, prerequisites are the edges, and use DFS to traverse graph, if cycle is found return False
# a cycle shows the courses are in a loop, meaning it's not possible to finish all


# Time complexity: O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq) # map each course to its prereqs

        visiting = set() # to track DFS path

        def dfs(course): # dfs each course
            if course in visiting:
                return False # cycle detected
            if adj[course] == []:
                return True # no prereqs

            visiting.add(course)
            # dfs each prereq
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False # if dfs traversal returns a cycle, return False
            # remove course from visited after processing
            visiting.remove(course)
            # reset prereq
            adj[course] = [] # done visiting already, if it's a neighbor of another, returns True automatically
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        
