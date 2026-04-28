# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ans = float('-inf')

        def maxDepthHelper(root: Optional[TreeNode], depth):
            # nonlocal ans
            # print(ans)
            if root == None:
                return 0

            if root.left == None and root.right == None:
                return depth 

            left_depth, right_depth = 0,0

            if root.left != None:
                left_depth = maxDepthHelper(root.left,depth+1)
            if root.right != None:
                right_depth = maxDepthHelper(root.right,depth+1)

            
            return max(left_depth, right_depth)

        return maxDepthHelper(root,1)   