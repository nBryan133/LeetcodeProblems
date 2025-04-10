# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #time complexity: O((n + m) * log(n + m))
    #space complexity: O(n + m)
        if(list1 == None):
            return list2
        elif(list2 == None):
            return list1

        ar = []

        while(list1 != None or list2 != None):
            if(list1 == None or list2 == None):
                if(list2 == None):
                    ar.append(list1.val)
                    list1 = list1.next
                else:
                    ar.append(list2.val)
                    list2 = list2.next
            else:
                if (list1.val <= list2.val):
                    ar.append(list1.val)
                    list1 = list1.next
                else:
                    ar.append(list2.val)
                    list2 = list2.next

        l = ListNode(ar[0])

        for i in range(len(ar) - 1, 0, -1):
            BufNode = ListNode(ar[i], l.next)
            l.next = BufNode

        return l
            

