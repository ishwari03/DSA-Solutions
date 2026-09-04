class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digcount=0
        for n in nums:
            digits=0
            while n>0:
                digits+=1
                n//=10
            if digits % 2==0:
                even_digcount+=1
        return even_digcount

