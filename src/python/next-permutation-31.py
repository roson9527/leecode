class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        check = False
        for i in range(length - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                check = True
                for j in range(length - 1, 0, -1):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        k = i
                        k_end = length - 1
                        while k < k_end:
                            nums[k], nums[k_end] = nums[k_end], nums[k]
                            k += 1
                            k_end -= 1
                        return

        if not check:
            nums.sort()
