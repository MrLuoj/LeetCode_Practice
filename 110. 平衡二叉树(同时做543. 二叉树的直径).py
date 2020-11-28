
# https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-%28iterative-and-recursive%29-both-beat-90

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return depth(root) != -1