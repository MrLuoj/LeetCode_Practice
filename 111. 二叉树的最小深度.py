
# https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36239/Python-BFS-and-DFS-solutions.

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1