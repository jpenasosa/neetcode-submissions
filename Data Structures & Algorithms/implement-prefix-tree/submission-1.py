class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.terminal: bool = False
    
    def insert(self, word: str):
        if not word:
            return

        char, rest = self._split(word)
        if char not in self.nodes:
            self.nodes[char] = TrieNode()
        
        if rest:
            self.nodes[char].insert(rest)
        else:
            self.nodes[char].terminal = True
    
    def search(self, word: str, ensure_terminal: bool = True) -> bool:
        char, rest = self._split(word)
        if char not in self.nodes:
            return False
        
        if rest:
            return self.nodes[char].search(rest, ensure_terminal)
        elif ensure_terminal:
            return self.nodes[char].terminal == True

        return True


    @staticmethod
    def _split(word: str) -> Tuple[str, str]:
        return word[0], word[1:]

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)

    def startsWith(self, prefix: str) -> bool:
        return self.root.search(prefix, ensure_terminal=False)
