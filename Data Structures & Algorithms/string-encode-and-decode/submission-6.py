class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += f"{len(string)}>{string}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            length, s = s.split('>', 1)
            length = int(length)
            string = s[:length]
            strs.append(string)
            s = s[length:]
        
        return strs

