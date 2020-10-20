
# https://leetcode-cn.com/problems/minimum-genetic-mutation/solution/dfshui-su-jie-ti-si-lu-dai-ma-yong-swift-by-zhen-y/
# https://leetcode.com/problems/minimum-genetic-mutation/discuss/189662/Python-BFS-%28same-as-word-ladder%29

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = []
        queue.append((start, 0))
        bankSet = set(bank)

        while queue:
            curr, step = queue.pop(0)
            if curr == end:
                return step
            for i in range(len(curr)):
                for c in "AGCT":
                    mutation = curr[:i] + c + curr[i + 1:]
                    if mutation in bankSet:
                        bankSet.remove(mutation)
                        queue.append((mutation, step + 1))

        return -1