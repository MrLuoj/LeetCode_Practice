
# https://leetcode.com/problems/spiral-matrix/discuss/20656/AC-Python-32ms-solution

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
        u, d, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while l < r and u < d:
            res.extend([matrix[u][j] for j in range(l, r)])
            res.extend([matrix[i][r] for i in range(u, d)])
            res.extend([matrix[d][j] for j in range(r, l, -1)])
            res.extend([matrix[i][l] for i in range(d, u, -1)])
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
        if l == r:
            res.extend([matrix[i][r] for i in range(u, d + 1)])
        elif u == d:
            res.extend([matrix[u][j] for j in range(l, r + 1)])
        return res