# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)

        if len(intervals) < 2:
            return intervals

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            new_tar = self.check(res[-1], intervals[i])
            if new_tar != None:
                res[-1] = new_tar
            else:
                res.append(intervals[i])

        return res

    def check(self, target, tmp):
        if target.end >= tmp.start:
            return Interval(min(target.start, tmp.start), max(target.end, tmp.end))
        else:
            return None
