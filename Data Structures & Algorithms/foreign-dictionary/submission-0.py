class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            word = words[i]
            nextWord = words[i+1]

            # ensure nextWord is not a prefix of word
            minLen = min(len(word), len(nextWord))
            if len(word) > len(nextWord) and word[:minLen] == nextWord[:minLen]:
                return ""

            for j in range(minLen):
                if word[j] != nextWord[j]:
                    adj[word[j]].add(nextWord[j])
                    break

        visit = {}
        res = []

        def dfs(node):
            if node in visit:
                return visit[node]
            
            visit[node] = True
            for child in adj[node]:
                if dfs(child):
                    return True
            
            res.append(node)
            visit[node] = False


        for c in adj:
            if dfs(c):
                return ""

        return "".join(reversed(res))



