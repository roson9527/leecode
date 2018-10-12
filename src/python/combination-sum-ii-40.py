class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.anslist = []
        self.DFS(candidates, target, 0, [])
        return self.anslist

    def DFS(self, cand, tar, start, value_list):
        if tar == 0 and value_list not in self.anslist:
            return self.anslist.append(value_list)
        for i in range(start, len(cand)):
            if cand[i] > tar:
                return
            self.DFS(cand, tar - cand[i], i+1, value_list+[cand[i]])
