import collections


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False

        count = len(s1)
        beg = 0
        p = count - 1

        tar = collections.Counter(s1)
        pool = collections.Counter(s2[0: count-1])

        while p < len(s2):
            pool[s2[p]] += 1
            # 两个字典一致
            if tar == pool:
                return True

            pool[s2[beg]] -= 1
            if pool[s2[beg]] == 0:
                del pool[s2[beg]]

            beg += 1
            p += 1

        return False
