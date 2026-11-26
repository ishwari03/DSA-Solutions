class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        turns = 0
        while n >= take:
            n = n - take
            take -= 1
            turns += 1
        return turns % 2 == 1