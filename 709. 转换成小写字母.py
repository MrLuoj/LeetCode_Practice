
# https://leetcode.com/problems/to-lower-case/discuss/213739/Python3-solution

# ord() ���ض�Ӧ�� ASCII ��ֵ
# chr() ��һ������������������һ����Ӧ���ַ���
class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                res += chr(ord(char) + 32)
            else:
                res += char
        return res