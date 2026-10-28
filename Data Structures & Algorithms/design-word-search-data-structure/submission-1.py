class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_end = True
    
    @staticmethod
    def _split(word):
        return word[0], word[1:]

    def search(self, word):
        c, remaining = self._split(word)
        if c == '.':
            if not remaining:
                return any(child.is_end for child in self.children.values())

            for child in self.children.values():
                match = child.search(remaining)
                if match:
                    return True
            return False
        else:
            if c not in self.children:
                return False
            
            child = self.children[c]
            if not remaining:
                return child.is_end
            return child.search(remaining)



class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)
        
