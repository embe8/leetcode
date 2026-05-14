# return valid order of courses to finish all courses (numCourses) required
# approach: same as course schedule problem, use dfs to check for cycles, courses not belonging to cycles are added to output
# Time complexity: O(V + E)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i: [] for i in range(numCourses)}
        for courses, prereq in prerequisites:
            adj[courses].append(prereq)

        output = []

        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle: return False
            if course in visited: return True

            cycle.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
        
