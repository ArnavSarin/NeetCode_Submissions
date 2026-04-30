# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        queue = [(root,float('-inf'), float('inf'))]

        while len(queue)>0:
            node, left, right = queue.pop(0)

            if node.val <= left or node.val >= right:
                return False

            if node.left is not None:
                queue.append((node.left,left,node.val))

            if node.right is not None:
                queue.append((node.right,node.val,right))

        return True