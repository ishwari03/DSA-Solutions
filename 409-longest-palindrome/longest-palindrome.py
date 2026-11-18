class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        has_odd_freq = False

        for count in freq.values():
            if count %2 ==0:
                res += count
            else:
                res += count - 1
                has_odd_freq = True
        if has_odd_freq:
            res += 1
        return res