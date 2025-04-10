class Solution:
    def trap(self, height: List[int]) -> int:
    #time complexity: O(N)
    #space complexity: O(N)
        n = len(height)
        l = [0] * n
        r = [0] * n
        l_height = 0
        r_height = 0

        for i in range(n):
            j = -i - 1
            l[i] = l_height
            r[j] = r_height

            l_height = max(l_height, height[i])
            r_height = max(r_height, height[j])

        t_water = 0
        for i in range(n):
            pot = min(l[i],r[i])
            t_water += max(0, pot - height[i])
        
        return t_water


                