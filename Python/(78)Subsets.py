class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    #time complexity: O(2^n)
    #space complexity: O(2^n)

        ans = [[]]
        
        for num in nums:
            ans += [curr + [num] for curr in ans]
        return ans