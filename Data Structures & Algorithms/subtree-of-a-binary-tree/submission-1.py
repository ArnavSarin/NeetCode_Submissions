# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a,b):
            
            if a is None and b is not None:
                return False
            
            if a is not None and b is None:
                return False

            if a is None and b is None:
                return True

            if a.val != b.val:
                return False

            check_left = isSameTree(a.left, b.left)
            check_right = isSameTree(a.right,b.right)

            if not check_left or not check_right:
                return False
            
            return True
        
        if root is not None and subRoot is None:
            return False

        if root is None and subRoot is not None:
            return False

        if root is None and subRoot is None:
            return True 

        check_middle = False
        if root.val == subRoot.val:
            check_middle = isSameTree(root,subRoot)
        
        check_left = self.isSubtree(root.left, subRoot)
        check_right = self.isSubtree(root.right, subRoot)

        return check_middle or check_left or check_right
        