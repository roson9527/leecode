class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            a, b = b, a

        b = [int(b[i]) for i in range(len(b))]
        a = [int(a[i]) for i in range(len(a))]
        b.insert(0, 0)

        for i in range(len(a)):
            b[len(b) - 1 - i] += a[len(a) - 1 - i]

        for i in range(len(b)-1, 0, -1):
            if b[i] >= 2:
                b[i] -= 2
                b[i-1] += 1

        if b[0] == 0:
            b = b[1:]

        res = [str(b[i]) for i in range(len(b))]

        return "".join(res)
