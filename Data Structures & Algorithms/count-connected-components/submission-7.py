class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        def find(u):
            res = u
            while res != parent[res]:
                res = parent[parent[res]]
            
            parent[u] = res
            return res

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return 0
            
            if rank[pu] >= rank[pv]:
                parent[pv] = find(pu)
                rank[pu] += rank[pv]
            else:
                parent[pu] = find(pv)
                rank[pv] += rank[pu]

            return 1
            
        ans = n
        for u, v in edges:
            ans -= union(u, v)
        
        return ans