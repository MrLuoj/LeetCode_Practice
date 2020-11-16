
# https://leetcode-cn.com/problems/counting-bits/solution/python3-si-chong-fang-fa-jie-jue-bi-te-wei-ji-shu-/

class Solution:
    def countBits(self, num: int) -> List[int]:

        res = []
        for i in range(num + 1):
            res.append(self.count_bit(i))
        return res

    def count_bit(self,n):
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

# ·¨¶þ
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(1,num+1):
            if (i%2 == 1):
                dp[i] = dp[i-1]+1
            else:
                dp[i] = dp[i//2]
        return dp
