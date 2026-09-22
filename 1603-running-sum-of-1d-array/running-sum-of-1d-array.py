class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ps = [0]*len(nums)
        ps[0]=nums[0]
        for i in range(1,len(nums)):
            ps[i]= ps[i-1] + nums[i]
        return ps