# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        queue = [(root,0)]
        levels = []

        while len(queue)>0:
            curr_node = queue.pop(0)

            if curr_node[0].left is not None:
                queue.append((curr_node[0].left,curr_node[1] + 1))
            if curr_node[0].right is not None:
                queue.append((curr_node[0].right,curr_node[1] + 1))
            
            if curr_node[1] < len(levels):
                levels[curr_node[1]].append(curr_node[0].val)
            else:
                levels.append([curr_node[0].val])
            

        return levels
        
            

        