from itertools import zip_longest

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True

        alphabet = dict(zip(order, range(len(order))))
        alphabet[""] = -1

        # Compare pairwise a word and the previous word in the list
        prev = words[0]
        for i in range(1, len(words)):
            cur = words[i]
            # Compare character by character
            for c1, c2 in zip_longest(prev, cur, fillvalue=""):
                if c1 == c2:
                    continue

                if alphabet[c2] < alphabet[c1]:
                    return False
                else:
                    break

            prev = cur

        return True