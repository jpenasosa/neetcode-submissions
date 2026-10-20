class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        lengths = []
        for word in strs:
            lengths.append(str(len(word)))

        return ",".join(lengths) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s or s == "#":
            return []

        strs = []
        lengths, words = s.split("#", 1)
        lengths = lengths.split(",")

        while lengths:
            length = int(lengths.pop(0))
            strs.append(words[:length])
            words = words[length:]
        
        return strs
