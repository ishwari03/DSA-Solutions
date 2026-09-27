class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #brute TC:O(n^2) SC:O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        #optimized- using hashset TC:O(n), SC:O(n)
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False