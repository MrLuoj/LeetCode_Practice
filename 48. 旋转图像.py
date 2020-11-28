
# https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-%281-to-7-lines%29

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
        return matrix


    