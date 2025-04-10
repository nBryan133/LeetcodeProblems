class Solution:
    def romanToInt(self, s: str) -> int:
    #time complexity: 0(N)
    #space complexity: 0(1)

        rNum = {'I' : 1, 'V': 5, 'X': 10, 
        'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and rNum[s[i]] < rNum[s[i + 1]]:
                ans -= rNum[s[i]]
            else:
                ans += rNum[s[i]]

        return ans
        

        