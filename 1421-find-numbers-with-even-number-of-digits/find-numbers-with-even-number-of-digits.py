class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for n in nums:
            if (n>=10 and n<=99) or (n>=1000 and n<=9999) or n==100000:
                c+=1
        return c