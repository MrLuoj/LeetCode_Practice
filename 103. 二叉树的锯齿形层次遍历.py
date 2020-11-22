
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/749036/Python-Clean-BFS-solution-explained

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        direction = 1
        while queue:
            cur_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_level[::direction])
            direction *= -1
        return res