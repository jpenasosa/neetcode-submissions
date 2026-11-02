class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:        
        if len(edges) < n - 1:
            return False

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = [False]*n
        visited = 0

        # Check for cycles
        def dfs(v, prev):
            if visit[v]:
                return True

            nonlocal visited
            visit[v] = True
            visited += 1

            for u in adj[v]:
                if u == prev:
                    continue

                if dfs(u, v):
                    return True

            return False
        
        has_cycle = dfs(0, -1)
        return visited == n and not has_cycle
