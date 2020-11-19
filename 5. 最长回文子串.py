
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-%28from-middle-to-two-ends%29.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i+1), res, key=len)
        return res

    def helper(self, s, l, r):
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]