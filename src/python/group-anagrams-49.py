class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}

        for s in strs:
            key = "".join(sorted(s))
            if not d.get(key):
                d[key] = []
            d[key].append(s)

        return list(d.values())
