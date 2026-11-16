class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [ [] for _ in range(n) ]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False]*n

        def traverse(u, prev):
            if visited[u]:
                return
            
            visited[u] = True

            for v in adj[u]:
                if v == prev:
                    continue

                traverse(v, u)

        ans = 0
        for u in range(n):
            if visited[u]:
                continue
            traverse(u, -1)
            ans += 1

        return ans
