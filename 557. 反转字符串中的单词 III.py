
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/solution/python-fan-zhuan-zi-fu-chuan-zhong-dan-ci-si-lu-xi/

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())