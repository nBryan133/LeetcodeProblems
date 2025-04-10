class Solution:
    def longestPalindrome(self, s: str) -> str:
    #time complexity: N(n^3)
    #Space complexity: N(n)

        if len(s) < 2:
            return s
        
        n = len(s)

        s = "^%" + s + "$&"

        o = [0] * (n + 4)
        e = [0] * (n + 4)
        mInd = 0
        mVal = 0

        #loop with two states one for an even length palindrome one for odd length
        for i in range(2, n + 2):
            while s[i - e[i]] == s[i + 1 + e[i]]:
                e[i] = e[i] + 1

            e[i] = e[i] * 2
                
            while s[i - o[i]] == s[i + o[i]]:
                o[i] = o[i] + 1 
            if o[i] > 1:
                o[i] = o[i] * 2 - 1

            buf = max(o[i], e[i])

            if mVal < buf:
                mInd = i
                mVal = buf
        
        if mVal % 2 == 0:
            return s[mInd - ((mVal - 2) // 2) : mInd + 1 + (mVal // 2)]
        else:
            return s[mInd - (mVal // 2) : mInd + (mVal // 2) + 1]

            
        