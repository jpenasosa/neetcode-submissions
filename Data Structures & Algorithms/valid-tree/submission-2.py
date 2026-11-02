class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:        
        if len(edges) < n - 1:
            return False

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = [False]*n
        recStack = [False]*n

        # Check for cycles
        def has_cycle(v, source):
            if recStack[v]:
                return True

            if visit[v]:
                return False
            
            visit[v] = True
            recStack[v] = True

            for u in adj[v]:
                if u == source:
                    continue

                if has_cycle(u, v):
                    return True
            
            recStack[v] = False

            return False

        for v in range(n):
            if not visit[v] and has_cycle(v, -1):
                return False
        
        return True
