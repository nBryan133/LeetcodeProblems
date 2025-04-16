# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #time complexity: O(N)
    #space complexity: O(N)
    #iterative approach

        #answer to build reverse list in initialized to None
        ans = None

        #while loop to travers through the Linked list and build out new list
        while head != None:
            new_Node = ListNode(head.val, ans) #create new Node to put in our list
            ans = new_Node                 #add new node to front of list
            head = head.next               #go to next pos in linked list
        
        #return new List
        return ans