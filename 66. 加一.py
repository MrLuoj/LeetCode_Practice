
# https://leetcode.com/problems/plus-one/discuss/24090/Python-simple-solution-using-recursion

class Solution(object):
    def plusOne(self, digits):
        if digits == []:  #just for case: digits = [9]
            return [1]
        if digits[-1] != 9:
            return digits[:-1]+[digits[-1]+1]
        else:
            return self.plusOne(digits[:-1])+[0]