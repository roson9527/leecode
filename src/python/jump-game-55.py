class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        pos = 0
        max_pos = len(nums) - 1
        while pos < max_pos:
            n = nums[pos]
            if n == 0:
                return False
            if n+pos >= max_pos:
                pos = max_pos
            else:
                max_len = 0
                max_i = 0
                for i in range(1, n + 1):
                    tmp = i+nums[pos+i]
                    if max_len < tmp:
                        max_i = i
                        max_len = tmp

                pos = pos + max_i

            total += 1

        return True
