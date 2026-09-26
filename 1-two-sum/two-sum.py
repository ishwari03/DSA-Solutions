class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #brute force approach- TC:O(n^2) SC:O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return[]

        #optimized-
        seen = {}  # maps number -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i    
        return []