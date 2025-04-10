class Solution:
#time complexity: O(N * M)
#space complexity: O(N * M)
    def isMatch(self, s: str, p: str) -> bool:

        #populate 2d array with Falses and sets the base case to True
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        cache[len(s)][len(p)] = True

        #iterates through s and p backwards
        for i in range(len(s), -1, -1):
            for j in range(len(p) -1, -1, -1):
                #is current position a match
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                #if next character is *
                if (j + 1 < len(p)) and p[j + 1] == '*':
                    #case for skipping the star and continuing on
                    cache[i][j] = cache[i][j + 2]

                    #if there is a match then set current positon to be True if either i + 1, j or skipping this * is true
                    if match:
                        cache[i][j] = cache[i + 1][j] or cache[i][j]
                #if thers a match then set the current position to be whatever i + 1, j + 1 was
                elif match:
                    cache[i][j] = cache[i + 1][j + 1]
                               
        return cache[0][0]
                    

        