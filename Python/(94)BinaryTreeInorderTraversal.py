# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #time complexity: O()
    #space complexity: O()

        #if root doesnt exist
        if root == None:
            return []

        #method to handle problem recursively
        def traverse(root):
            #buf to hold answer
            buf = []
            #base case (if we cant traverse any further)
            if root.left == None and root.right == None:
                buf.append(root.val)
            else:
                #if we can traverse right then traverse that branch and add that list of values to buf
                if root.left != None:
                    buf.extend(traverse(root.left))
                
                #add the current root val after left values if they exist
                buf.append (root.val)

                #if more values are to the right then we traverse that side of the tree and add those values to buf
                if root.right != None:
                    buf.extend(traverse(root.right))
            
            return buf

        #call and return output of traversal
        return traverse(root)