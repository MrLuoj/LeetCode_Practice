
# https://leetcode-cn.com/problems/validate-binary-search-tree/solution/xiong-mao-shua-ti-python3-tan-xin-wei-hu-ke-da-d-5/


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursion(root, min_value, max_value):
            if not root:
                return True
            if root.val <= min_value or root.val >= max_value:
                return False
            return recursion(root.left, min_value, root.val) and recursion(root.right, root.val, max_value)
        return recursion(root, float("-inf"), float("inf"))