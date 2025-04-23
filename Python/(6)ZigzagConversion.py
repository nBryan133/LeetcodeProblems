class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #time complexity: O(N)
        #space complexity: O(N)
        ans = [[''] * numRows]
        
        if numRows == 1:
            return s

        n = len(s)
        i = 0
        j = 0
        t = 0
        climbing = False

        while i < len(s):
            
            if not climbing:
                ans[j][t] = s[i]
                
                if t < numRows - 1:
                    t += 1
                else:
                    climbing = True
                    j += 1
                    t -= 1
                i += 1
            else:
                ans.append([''] * numRows)
                ans[j][t] = s[i]

                if t > 0:
                    j += 1
                    t -= 1
                else:
                    climbing = False
                    t += 1
                i += 1

        return ''.join(char for pair in zip(*ans) for char in pair)
