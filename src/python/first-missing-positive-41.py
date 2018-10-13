class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lt = len(nums)
        for i in range(lt):
            if 0 < nums[i] and nums[i] < len(nums):
                while nums[i] != i+1:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                    if nums[i] <= 0 or nums[i] >= lt or nums[i] == nums[nums[i] - 1]:
                        break

        for i in range(lt):
            if nums[i] != i+1:
                return i+1

        return lt+1
