class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    #time complexity: 0(N * M)
    #space complexity: 0(1)
        ans = strs[0]

        for str in strs:
            if(len(ans) > len(str)):
                ans = ans[0:len(str)]
                
            for i in range(min(len(ans), len(str))):
                if(i != 0 and str[i] != ans[i]):
                    ans = str[0:i]
                    break
                elif(i == 0 and str[i] != ans[i]):
                    return ""
        return ans