class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # res = []
        # for num in nums:
        #     res.append(num * num)
        #     res.sort()
        # return res
    
        n = len(nums)
        res = [0] * n

        left = 0
        right = n - 1
        pos = n - 1  # fill from largest square (end) to smallest (start)

        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                res[pos] = left_sq
                left += 1
            else:
                res[pos] = right_sq
                right -= 1

            pos -= 1

        return res