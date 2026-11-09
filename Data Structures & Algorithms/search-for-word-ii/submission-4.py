class PrefixNode:
    def __init__(self):
        self.children = {}

    def add(self, word: str):
        if not word:
            return

        c = word[0]
        if c not in self.children:
            self.children[c] = PrefixNode()

        self.children[c].add(word[1:])


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        ans = set()
        word_set = set(words)

        # Build prefix tree
        root = PrefixNode()
        for word in words:
            root.add(word)

        def dfs(r, c, node, prefix, path):
            if (
                r not in range(rows)
                or c not in range(cols)
                or board[r][c] not in node.children
                or (r,c) in path
            ):
                return

            char = board[r][c]
            node = node.children[char]
            word = prefix + char

            if word in word_set:
                ans.add(word)
            
            path.add((r, c))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r + dr, c + dc, node, word, path)
            
            path.remove((r, c))


        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "", set())

        return list(ans)
