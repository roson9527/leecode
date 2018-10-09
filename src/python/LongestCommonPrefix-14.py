class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix = ""
        for i in range(len(strs[0])):
            prefix += strs[0][i]
            for indx in range(1, len(strs)):
                if not strs[indx].startswith(prefix):
                    return prefix[:-1]

        return prefix
