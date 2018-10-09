class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        abs_nums = {}
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                abs_nums[abs(s - target)] = s
                if s > target:
                    k -= 1
                else:
                    j += 1
        key_zero = ([i for i in abs_nums.keys()])
        key_zero.sort()
        return abs_nums.get(key_zero[0])
