class Solution:
    def isPalindrome(self, x: int) -> bool:
    #time complexity: 0(n)
    #space complexity: 0(1)
        
        if(x < 0):
            return False

        a = x
        n = 0

        while a > 0:
            n = n * 10 + a % 10
            a = a // 10
        
        if(n == x):
            return True
        return False
