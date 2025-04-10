class Solution:
    def reverse(self, x: int) -> int:
    #time Complexity: O(log(N))
    #Space Complexity: O(1)
        sign = -1 if x < 0 else 1
        x = abs(x)
        buf = 0
        while x > 0:
            digit = x % 10
            buf = buf * 10 + digit
            x //= 10
        buf = buf * sign
        if buf > 2 ** 31 - 1 or buf < (-2 ** 31):
            return 0
        return buf