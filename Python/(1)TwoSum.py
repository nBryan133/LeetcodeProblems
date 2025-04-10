def twoSum(self, nums, target):
#time complexity: O(n)
#space complexity 0(n)
    hashmap = {}

    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        complement = target - nums[i]
        if(complement in hashmap and hashmap[complement] != i):
            return [i, hashmap[complement]]
    
    return []