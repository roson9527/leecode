import math


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        start_cur = self.findFrist(nums, target)
        end_cur = self.findLast(nums, target)
        return [start_cur, end_cur]

    def findFrist(self, nums, target):
        lt = len(nums)
        start_cur = 0
        end_cur = lt - 1

        while start_cur < end_cur:
            mid = int((start_cur + end_cur) / 2)
            if nums[mid] >= target:
                end_cur = mid
            else:
                start_cur = mid + 1

        if nums[start_cur] != target:
            return -1

        return start_cur

    def findLast(self, nums, target):
        lt = len(nums)
        start_cur = 0
        end_cur = lt - 1

        while start_cur < end_cur:
            mid = math.ceil((start_cur + end_cur) / 2)
            if nums[mid] <= target:
                start_cur = mid
            else:
                end_cur = mid - 1

        if nums[start_cur] != target:
            return -1

        return start_cur
