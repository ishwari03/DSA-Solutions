from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have = Counter(text)  #countText
        need = Counter("balloon")    #balloon

        res = len(text) # or float('inf')
        
        for c in need:
            times = have[c] // need[c]
            res = min(res, times)
        return res