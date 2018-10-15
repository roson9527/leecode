class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.ant = []
        self.perm(nums, 0, len(nums))
        return self.ant

    def perm(self, nums, begin, end):
        if begin >= end:
            self.ant.append(nums[:])
        else:
            i = begin
            for n in range(begin, end):
                if n != i and nums[n] == nums[i]:
                    continue
                nums[n], nums[i] = nums[i], nums[n]
                self.perm(nums, begin+1, end)
                nums[n], nums[i] = nums[i], nums[n]
