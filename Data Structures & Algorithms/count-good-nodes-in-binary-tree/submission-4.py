# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        queue = [(root,root.val)]

        count = 1

        while len(queue)>0:
            node = queue.pop(0)

            if node[0].left is not None:
                max_val = node[1]
                if node[1] <= node[0].left.val:
                    print("GOT HERE 0")
                    print(node[0].left.val)
                    max_val = node[0].left.val
                    count+=1
                queue.append((node[0].left, max_val))

            if node[0].right is not None:
                max_val = node[1]
                if node[1] <= node[0].right.val:
                    print("GOT HERE 1")
                    print(node[0].right.val)
                    max_val = node[0].right.val
                    count+=1
                queue.append((node[0].right, max_val))
        
        return count