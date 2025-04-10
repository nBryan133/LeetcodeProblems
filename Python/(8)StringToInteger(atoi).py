class Solution:
    def myAtoi(self, s: str) -> int:
    #Time complexity: O(N)
    #Space complexity: O(1)

        s = s.lstrip()

        if len(s) == 0:
            return 0

        i = 0
        match s[i]:
            case "-":
                sign = -1
                i += 1
            case "+":
                sign = 1
                i += 1
            case _:
                sign = 1

        buf = 0

        while i < len(s) and s[i].isdigit() == True and buf < 2**31:
            buf = buf * 10 + (int(s[i]))
            i += 1

        buf = buf * sign
        if buf > 2**31 - 1:
            return 2**31 - 1
        elif buf < -2**31:
            return -2**31

        return buf