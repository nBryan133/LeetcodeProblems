class Solution:
    #time complexity: O(N^2)
    #space complexity: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        nums.sort()

        tuples = []

        for i in range(len(nums) - 1):
            if(i > 0  and nums[i] == nums[i - 1]):
                continue
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            
            while (l < r):
                if nums[l] + nums[r] == target:
                    tuples += [[nums[i], nums[l], nums[r]]]
                    
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return tuples