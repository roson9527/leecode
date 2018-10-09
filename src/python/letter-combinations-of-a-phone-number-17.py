class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict_num = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        str_num = str(digits)
        if len(str_num) == 0:
            return []

        zero = dict_num.get(str_num[0])
        res_list = [zero[i] for i in range(len(zero))]

        for i in range(1, len(str_num)):
            n = dict_num.get(str_num[i])
            tmp = []
            for indx in range(len(n)):
                c = n[indx]
                tmp.extend([ety+c for ety in res_list])
            res_list = tmp

        return res_list
