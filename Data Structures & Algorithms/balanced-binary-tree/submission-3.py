# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalanced_helper(root):

            if root is None:
                return (True, 0)

            check_left, height_left = isBalanced_helper(root.left)
            check_right, height_right = isBalanced_helper(root.right)

            check = check_left and check_right and abs(height_left - height_right) <= 1

            return (check, max(height_left,height_right) + 1)

        ans = isBalanced_helper(root)
        return ans[0]