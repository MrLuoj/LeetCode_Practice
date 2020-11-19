
# https://leetcode.com/problems/valid-palindrome-ii/discuss/107718/Easy-to-Understand-Python-Solution

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                one, two = s[l:r], s[l+1:r+1]
                return one == one[::-1] or two == two[::-1]
            l += 1
            r -= 1
        return True