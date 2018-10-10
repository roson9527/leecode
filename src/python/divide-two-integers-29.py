class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = (2 << 30) - 1
        MIN_INT = - (2 << 30)

        if divisor == 0 or (dividend == MIN_INT and divisor == -1):
            return MAX_INT

        div_sign = -1

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            div_sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        divs_tmp = divisor
        cnt = 0  # ** num

        while divs_tmp < dividend:
            divs = divs_tmp << 1
            if divs <= dividend:
                cnt += 1
                divs_tmp = divs
            else:
                break

        div_num = 0
        while cnt >= 0:
            if dividend >= divs_tmp:
                dividend -= divs_tmp
                if cnt > 0:
                    div_num += 2 << (cnt - 1)
                else:
                    div_num += 1
            else:
                cnt -= 1
                divs_tmp = divs_tmp >> 1

        return div_num * div_sign
