class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n== 0:
            return 0
        off = 0
        res = 1
        cm = 1

        while cm < n:
            if nums[cm] == nums[cm -1]:
                cm += 1
                continue
            nums[off + 1] = nums[cm]
            off += 1
            res += 1
            cm += 1
        return res 