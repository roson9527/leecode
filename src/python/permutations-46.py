class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ant = []
        self.perm(nums, 0, len(nums))
        return self.ant

    def perm(self, nums, begin, end):
        if begin >= end:
            self.ant.append(nums[:])
        else:
            i = begin
            for n in range(begin, end):
                nums[n], nums[i] = nums[i], nums[n]
                self.perm(n, begin+1, end)
                nums[n], nums[i] = nums[i], nums[n]
