
# https://leetcode.com/problems/reverse-words-in-a-string/discuss/47726/My-Accept-Answer-of-Python-with-one-line

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])