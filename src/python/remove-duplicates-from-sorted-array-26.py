class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        core = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            n = nums[i]
            if n == core:
                nums.pop(i)
            else:
                core = n

        return len(nums)
