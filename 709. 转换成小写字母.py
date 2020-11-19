
# https://leetcode.com/problems/to-lower-case/discuss/213739/Python3-solution

# ord() 返回对应的 ASCII 数值
# chr() 用一个整数作参数，返回一个对应的字符。
class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                res += chr(ord(char) + 32)
            else:
                res += char
        return res