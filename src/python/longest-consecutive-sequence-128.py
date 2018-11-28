class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maps = {}
        for i in nums:
            maps[i] = True

        max_count = 0
        while len(maps) > 0:
            keys = maps.keys()
            key = list(keys)[0]
            maps.pop(key)
            count = 1
            for i in range(1, len(keys)+1):
                if key - i in maps:
                    maps.pop(key - i)
                    count += 1
                else:
                    break

            for i in range(1, len(keys)+1):
                if key + i in maps:
                    maps.pop(key + i)
                    count += 1
                else:
                    break

            max_count = max(max_count, count)

        return max_count
