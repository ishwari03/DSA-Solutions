from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # have = Counter(text)  #countText
        # need = Counter("balloon")    #balloon
        have={}
        need={}
        for ch in text:
            have[ch] = have.get(ch,0) + 1
        for ch in "balloon":
            need[ch] = need.get(ch,0) + 1

        res = len(text) # or float('inf')
        
        for c in need:
            times = have.get(c,0) // need[c]
            res = min(res, times)
        return res