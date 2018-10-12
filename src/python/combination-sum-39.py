class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.anslist = []

    def DFS(self, cand, tar, start, value_list):
        if tar == 0:
            return self.anslist.append(value_list)
        for i in range(start, len(cand)):
            if cand[i] > tar:
                return
            self.DFS(cand, tar - cand[i], i, value_list+[cand[i]])
