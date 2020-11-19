
# https://leetcode-cn.com/problems/reverse-string/solution/python3-liang-chong-fang-fa-shi-xian-fan-zhuan-zi-/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s