class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    #Time complexity: O(N)
    #Space complexity O(N)
        presNums = {}

        for i in range(len(nums)):
            if nums[i] not in presNums:
                presNums.update({nums[i]: len(presNums) + 1})
        
        c = 0
        for val in presNums:
            nums[c] = val
            c = c + 1

        return len(presNums)