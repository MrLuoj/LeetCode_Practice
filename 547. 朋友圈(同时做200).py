
# https://leetcode.com/problems/friend-circles/discuss/903713/Python-Intuitive-DFS-Solutionor-Runtime-Faster-than-98-Solution

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        visited = [0] * len(M)
        circles = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M, visited, i)
                circles += 1
        return circles

    def dfs(self,M, visited, i):
        # dfs will terminate using the for loop
        for j in range(len(M[0])):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)