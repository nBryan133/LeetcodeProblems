# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    #time complexity: O(N)
    #space complexity: O(N)

        #post traversal recursive method
        def dFinder(node):
            if node == None:
                return 0
            else:
                return max(dFinder(node.left) + 1, dFinder(node.right) + 1)

        return dFinder(root)