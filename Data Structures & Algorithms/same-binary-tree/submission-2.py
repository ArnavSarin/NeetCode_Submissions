# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is not None:
            return False
        
        if q is None and p is not None:
            return False

        if q is None and p is None:
            return True

        if p.val != q.val:
            return False

        check_left = self.isSameTree(p.left, q.left)
        check_right = self.isSameTree(p.right,q.right)

        if not check_left or not check_right:
            return False

        return True

        
        