
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/211683/Python-3-Clean-and-Correct

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        chars = set()
        while l < len(s) and r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
                longest = max(longest, r - l)
            else:
                chars.remove(s[l])
                l += 1
        return longest