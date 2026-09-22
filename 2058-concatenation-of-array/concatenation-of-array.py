class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # return nums+nums
        ans=[]
        for _ in range(2):
            for n in nums:
                ans.append(n)
        return ans