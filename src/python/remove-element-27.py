class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            if n == val:
                nums.pop(i)

        return len(nums)
