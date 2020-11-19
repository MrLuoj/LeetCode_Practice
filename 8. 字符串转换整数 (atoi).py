
# https://leetcode.com/problems/string-to-integer-atoi/discuss/4653/Python-solution-based-on-RegEx

# ÕÆÎÕre.findall
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        str = s.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)
        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result

        except:
            return 0