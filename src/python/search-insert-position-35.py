class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start_cur = 0
        end_cur = len(nums) - 1

        if len(nums) == 0 or nums[0] >= target:
            return 0

        while start_cur <= end_cur:
            mid = int((start_cur+end_cur)/2)
            if nums[mid] < target:
                start_cur = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                end_cur = mid - 1

        return start_cur
