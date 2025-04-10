class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
    #Time Complexity: O(N + M)
    #Space Complexity: O(N + M)

        l = len(nums1) + len(nums2)

        arr = [0] * l

        pos1 = 0
        pos2 = 0

        for i in range(l):
            if(pos1 < len(nums1) and pos2 < len(nums2)):
                if(nums1[pos1] > nums2[pos2]):
                    arr[i] = nums2[pos2]
                    pos2 += 1
                elif(nums2[pos2] > nums1[pos1]):
                    arr[i] = nums1[pos1]
                    pos1 += 1
                else:
                    arr[i] = nums1[pos1]
                    pos1 += 1
            else:
                if(pos1 < len(nums1)):
                    arr[i] = nums1[pos1]
                    pos1 += 1
                else:
                    arr[i] = nums2[pos2]
                    pos2 += 1

        if(l % 2 == 0):
            avg = (float)(arr[(l / 2) - 1] + arr[l/2])
            res = avg / 2.0
            return res
        else:
            return arr[l - (l/2) - 1]