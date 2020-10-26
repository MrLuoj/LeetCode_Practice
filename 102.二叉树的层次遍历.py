
from collections import deque

class Solution:
    def levelOrder(self, root:TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            cur_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_level)
        return res