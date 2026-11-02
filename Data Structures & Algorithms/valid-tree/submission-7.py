class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:        
        if len(edges) < n - 1:
            return False

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()

        # Check for cycles
        def dfs(v, prev):
            if v in visit:
                return True

            visit.add(v)

            for u in adj[v]:
                if u == prev:
                    continue

                if dfs(u, v):
                    return True

            return False
        
        has_cycle = dfs(0, -1)
        return len(visit) == n and not has_cycle
