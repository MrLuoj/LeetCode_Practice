
# https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/359949/Python-recursive-and-iterative-solution

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1