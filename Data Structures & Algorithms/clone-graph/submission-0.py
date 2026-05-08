"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node == None: 
            return None

        head = Node(node.val)
        seen = {node.val: head}
        queue = deque([(head, node)])

        while len(queue) > 0:
            new_node, old_node = queue.popleft()

            for i in old_node.neighbors:
                if i.val not in seen:
                    temp_node = Node(i.val)
                    new_node.neighbors.append(temp_node)
                    seen[i.val] = temp_node
                    queue.append((temp_node,i))
                else:
                    new_node.neighbors.append(seen[i.val])
        
        return head


                    

            

        