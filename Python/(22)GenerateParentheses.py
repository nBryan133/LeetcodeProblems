class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    #time complexity: O(4^n / sqrt(n))
    #space complexity: O(N)
        ans = []

        def backtrack(l, r, s):
            if l < r or l > n or r > n:
                return
            if l == n and r == n:
                ans.append(s)
                return
            
            backtrack(l + 1, r, s + '(')
            backtrack(l, r + 1, s + ')')

        backtrack( 0, 0, '')

        return ans