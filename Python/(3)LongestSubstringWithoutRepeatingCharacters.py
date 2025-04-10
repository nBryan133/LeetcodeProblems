class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    #time complexity: O(n^3)
    #space complexity: O(n)

        subSts = []

        for i in range(len(s)):
            for n in range(i, len(s) + 1):
                if(n == i):
                    sub = [s[n]]
                elif(n == len(s) or sub.count(s[n]) > 0):
                    if(len(subSts) == 0 or len(sub) > len(subSts[-1])):
                        subSts.append(sub)
                    break
                else:
                    sub.append(s[n])


        if(len(subSts) == 0):
            return 0
        return len(subSts[-1])