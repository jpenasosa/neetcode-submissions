class CountSquares:

    def __init__(self):
        self.rows = {}

    def add(self, point: List[int]) -> None:
        x, y = point

        cols = self.rows.get(y)
        if not cols:
            self.rows[y] = {}
        
        self.rows[y][x] = 1 + self.rows[y].get(x, 0)

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point

        if not self.rows.get(y1):
            return res

        for x2 in self.rows[y1]:
            if x2 == x1:
                continue

            s = abs(x2 - x1)
            cnt = self.rows[y1][x2]
            for y2 in self.rows:
                if y2 == y1 or abs(y2 - y1) != s:
                    continue

                row = self.rows[y2]
                if x1 in row and x2 in row:
                    res += cnt * row[x1] * row[x2]

        return res