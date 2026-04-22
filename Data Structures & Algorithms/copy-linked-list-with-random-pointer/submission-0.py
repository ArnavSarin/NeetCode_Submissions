"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {None: None}
        ptr = head
        while ptr is not None:
            hm[ptr] = Node(ptr.val)
            ptr = ptr.next

        ptr = head 
        while ptr is not None:
            curr = hm[ptr]
            curr.next = hm[ptr.next]
            curr.random = hm[ptr.random]
            ptr = ptr.next

        return hm[head]








        

        

        
        