# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
      def preorderTraversal(self, root,lst=None):
        if not lst: 
            lst = []
        if root!=None:

            lst.append(root.val)
            self.preorderTraversal(root.left,lst)
            self.preorderTraversal(root.right,lst)
        return lst


            
        