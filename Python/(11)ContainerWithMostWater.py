class Solution:
    def maxArea(self, height: List[int]) -> int:
    #Time complexity: O(N)
    #Space complexity: O(1)

        p1 = 0
        p2 = len(height) - 1

        max_area = 0

        while p1 < p2:
           
            max_area = max(max_area, (p2 - p1) * (min(height[p1], height[p2])))
            
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_area
