class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        str_res = [0 for _ in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                str_res[i+j] += int(num1[i])*int(num2[j])

        # 进位处理(从低到高)
        result = ""
        up = 0
        for i in str_res:
            now = i + up
            cur = now % 10
            up = int(now / 10)
            result = str(cur) + result

        return result.lstrip('0')
