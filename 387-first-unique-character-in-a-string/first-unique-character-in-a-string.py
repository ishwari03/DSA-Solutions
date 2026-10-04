class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for ch in s: #for counting freq of each char
            count[ch] = count.get(ch,0) + 1 
        # Find the first character with frequency 1
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i 
        return -1