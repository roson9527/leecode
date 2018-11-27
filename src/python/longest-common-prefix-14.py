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

        strs.sort()
        if len(strs[0]) == 0:
            return ""

        ret = ""
        for i in range(len(strs[0])):
            val = strs[0][i]

            flag = True
            for j in range(1, len(strs)):
                if strs[j][i] != val:
                    flag = False
                    break

            if flag:
                ret = strs[0][:i+1]
            else:
                break

        return ret
