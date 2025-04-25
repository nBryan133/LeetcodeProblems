class Solution:
    #time complexity: O(3N * 4M)
    #space complexity: O(3N * 4M)
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []

        ht = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        def cBuild(i, curStr):
            if i == len(digits):
                ans.append(curStr)
                return ans
            for c in ht[digits[i]]:
                cBuild(i + 1, curStr + c)

        cBuild(0, "")
        return ans

