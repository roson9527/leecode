class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        p = 0
        max_len = 1
        while p+1 < len(nums):
            if nums[p] < nums[p+1]:
                pp = p+1
                while pp+1 < len(nums):
                    if nums[pp+1] <= nums[pp]:
                        break
                    pp += 1

                max_len = max(pp - p + 1, max_len)
                p = pp
            else:
                p += 1

        return max_len
