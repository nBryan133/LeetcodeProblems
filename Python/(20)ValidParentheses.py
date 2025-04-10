class Solution:
    def isValid(self, s: str) -> bool:
    #Time complexity: O(N)
    #Space complexity: O(1)
        p = 0
        b = 0
        sg = 0

        for c in s:
            match c:
                case '(':
                    p += 1 + b + sg
                    
                case '[':
                    b += 1 + p + sg
                    
                case '{':
                    sg += 1 + p + b
                    
                case ')':
                    if( p > 0 and p > b and p > sg):
                        p -= 1 + b + sg
                        
                    else:
                        return False
                case ']':
                    if( b > 0 and b > p and b > sg):
                        b -= 1 + p + sg
                        
                    else:
                        return False
                case '}':
                    if( sg > 0 and sg > b and sg > p):
                        sg -= 1 + b + p
                        
                    else:
                        return False

        return p + b + sg == 0