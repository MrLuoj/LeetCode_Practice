
# https://leetcode.com/problems/length-of-last-word/discuss/847535/Python-solution-without-split-explained

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end >= 0 and s[end] == " ":
            end -= 1
        begin = end
        while begin >= 0 and s[begin] != " ":
            begin -= 1
        return end - begin