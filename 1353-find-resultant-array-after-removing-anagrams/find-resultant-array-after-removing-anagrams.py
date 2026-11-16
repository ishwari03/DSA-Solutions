class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        res = []
        res.append(words[0])
        for word in words[1:]:
            if sorted(word) == sorted(res[-1]):
                continue
            else:
                res.append(word)
        return res