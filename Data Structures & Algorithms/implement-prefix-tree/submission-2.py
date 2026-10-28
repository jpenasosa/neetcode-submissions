class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.is_end: bool = False


def _split(word: str) -> Tuple[str, str]:
    return word[0], word[1:]

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.nodes:
                cur.nodes[c] = TrieNode()
            cur = cur.nodes[c]
        
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
        
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
        
        return True

