class Solution:
    def intToRoman(self, num: int) -> str:
    #time complexity: O(N)
    #Space complexity: O(N)

        hm = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
        ans = ""
        pos = 1

        while(num > 0):
            buf = (num % 10)

            if(buf >= 5):
                match buf:
                    case 9:
                        ans += hm[10 * pos] + hm[1 * pos]
                    case _:
                        ans += hm[1 * pos] * (buf - 5)
                        ans += hm[5 * pos]
                        
            else:
                match buf:
                    case 4:
                        ans += hm[5 * pos] + hm[1 * pos] 
                    case _:
                        ans += hm[1 * pos] * buf
            num = num // 10
            pos *= 10
        return ans[::-1]