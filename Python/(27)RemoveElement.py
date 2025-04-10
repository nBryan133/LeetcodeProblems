class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    #Time complexity: O(N)
    #Space complexity: O(N)

        newAr = []

        for num in nums:
            #print(num)
            if(num != val):
                newAr.append(num)
            #print(newAr)
            
        nums[:] = newAr + nums[len(newAr):]

        print(nums)
        print(len(newAr))

        return len(newAr)