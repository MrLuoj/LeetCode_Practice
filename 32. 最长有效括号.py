
# https://leetcode.com/problems/longest-valid-parentheses/discuss/14312/My-ten-lines-python-solution

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i+1] = dp[p] + i - p + 1
        return max(dp)