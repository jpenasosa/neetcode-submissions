from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Build graph
        town = defaultdict(set)
        for a, b in trust:
            town[a].add(b)
        
        people = set(range(1, n + 1))
        maybe_judge = people - set(town)
        if len(maybe_judge) != 1:
            return - 1

        judge = maybe_judge.pop()
        for trust_set in town.values():
            if judge not in trust_set:
                return -1
        
        return judge
        