# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        arr = []
        heapq.heapify(arr)

        while len(stack)>0:
            node = stack.pop()
            heapq.heappush(arr, node.val)

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)

        ans = -1
        print(arr)
        for i in range(0,k):
            ans = heapq.heappop(arr)
        
        return ans

