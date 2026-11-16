from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0

        for x2, y2 in self.points:
            if x2 == x1 or y2 == y1 or abs(y2-y1) != abs(x2-x1):
                continue

            if (x2, y1) not in self.points or (x1, y2) not in self.points:
                continue

            res += self.points[(x2, y2)] * self.points[(x2, y1)] * self.points[(x1, y2)] 
        
        return res
