class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        word = strs[0]

        for i, char in enumerate(word):
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return prefix
                
            prefix += char
        
        return prefix
