class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            if current < 0:
                current = nums[i]
            else:
                current += nums[i]

            if current > total:
                total = current

        return total
