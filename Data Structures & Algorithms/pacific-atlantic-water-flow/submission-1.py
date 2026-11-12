class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        for c in range(cols):
            pacific.add((0, c))
            atlantic.add((rows-1, c))
        
        for r in range(rows):
            pacific.add((r, 0))
            atlantic.add((r, cols-1))
        
        def dfsFill(r, c, prev):
            if (
                r not in range(rows)
                or c not in range(cols)
                or (r, c) in proc
                or heights[r][c] < prev
            ):
                return

            proc.add((r, c))

            dfsFill(r+1, c, heights[r][c])
            dfsFill(r-1, c, heights[r][c])
            dfsFill(r, c+1, heights[r][c])
            dfsFill(r, c-1, heights[r][c])


        proc = set()
        for (r, c) in pacific:
            dfsFill(r, c, heights[r][c])
        
        pacific.update(proc)
        
        proc = set()
        for (r, c) in atlantic:
            dfsFill(r, c, heights[r][c])
        
        atlantic.update(proc)

        return [ list(p) for p in pacific & atlantic ]