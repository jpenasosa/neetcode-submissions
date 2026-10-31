class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        # Build adjacency list
        for (course, prereq) in prerequisites:
            adj[prereq].append(course)

        def dfs(adj, u, visited, recStack):
            # Node is already in the current DFS path
            if recStack[u]:
                return True

            # Node is already visited
            if visited[u]:
                return False

            visited[u] = True
            recStack[u] = True

            # Visit all adjacent nodes
            for v in adj[u]:
                if dfs(adj, v, visited, recStack):
                    return True

            # Remove node from current DFS path
            recStack[u] = False

            return False
        
        def isCyclic(adj):
            V = len(adj)

            visited = [False] * V
            recStack = [False] * V

            # Check all components
            for i in range(V):
                if not visited[i] and dfs(adj, i, visited, recStack):
                    return True

            return False

        return not isCyclic(adj)
