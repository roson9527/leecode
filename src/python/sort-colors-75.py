class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        beg_p = 0
        end_p = len(nums) - 1
        p = 0

        while p <= end_p:
            val = nums[p]
            if val == 2:
                nums[p], nums[end_p] = nums[end_p], nums[p]
                end_p -= 1
                continue

            if val == 0:
                nums[p], nums[beg_p] = nums[beg_p], nums[p]
                beg_p += 1

            p += 1
