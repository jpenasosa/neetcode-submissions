class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def _search(self, word: str, start: int, root: TrieNode) -> bool:
        cur = root
        for i in range(start, len(word)):
            c = word[i]

            if c == '.':
                for child in cur.children.values():
                    if self._search(word, i+1, child):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                cur = cur.children[c]

        return cur.is_end
    
    def search(self, word: str) -> bool:
        return self._search(word, 0, self.root)
        
