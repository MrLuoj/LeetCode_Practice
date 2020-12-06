
# https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/332356/Python-O%28m+n%29-Linear-Search-from-Top-Right-Corner

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
            else:
                return True
        return False