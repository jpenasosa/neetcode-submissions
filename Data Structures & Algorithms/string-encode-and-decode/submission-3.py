class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"

        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            length, rest = s.split("#", 1)
            length = int(length)
            strs.append(rest[:length])
            s = rest[length:]
        
        return strs
