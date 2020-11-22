
# https://leetcode.com/problems/binary-tree-right-side-view/discuss/56248/Python-easy-to-understand-BFS-solution-%28level-by-level

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        global node
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            val = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(val)
        return res