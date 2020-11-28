
# https://leetcode.com/problems/symmetric-tree/discuss/33068/6line-AC-python

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root == None or self.recursion(root.left, root.right)

    def recursion(self, L, R):
        if L and R and L.val == R.val:
            return self.recursion(L.left, R.right) and \
                   self.recursion(L.right, R.left)
        return L == R


    