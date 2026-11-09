class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        ans = set()
        visit = set()

        # Build prefix tree
        root = TrieNode()
        for word in words:
            root.add(word)

        def dfs(r, c, node, prefix=""):
            if (
                r not in range(rows)
                or c not in range(cols)
                or board[r][c] not in node.children
                or (r,c) in visit
            ):
                return

            char = board[r][c]
            node = node.children[char]
            word = prefix + char

            if node.is_end:
                ans.add(word)

            visit.add((r, c))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r + dr, c + dc, node, word)
            
            visit.remove((r, c))


        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return list(ans)
