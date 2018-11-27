class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.DFS(0, s, [])
        return self.result

    def DFS(self, length, src, ips=[]):
        if length == 4:
            if src == "":
                self.result.append(".".join(ips))
            return

        if src == "":
            return

        self.DFS(length+1, src[1:], ips+[src[:1]])
        if src[0] != "0":
            if len(src) >= 2:
                self.DFS(length+1, src[2:], ips+[src[:2]])
            if len(src) >= 3 and int(src[:3]) <= 255:
                self.DFS(length+1, src[3:], ips+[src[:3]])
