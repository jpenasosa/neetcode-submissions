class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(v, prev):
            if v in visit:
                return
            
            visit.add(v)

            for u in adj[v]:
                if u == prev:
                    continue

                dfs(u, v)

        # Track number of times we had to traverse connected nodes
        ans = 0
        i = 0
        while len(visit) < n:
            if i in visit:
                i += 1
            else:
                dfs(i, -1)
                ans += 1
        
        return ans