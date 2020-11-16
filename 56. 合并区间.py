
# https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for i in sorted(intervals, key = lambda i: i[0]):
            if res != [] and i[0] <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], i[-1])
            else:
                res.append(i)
        return res