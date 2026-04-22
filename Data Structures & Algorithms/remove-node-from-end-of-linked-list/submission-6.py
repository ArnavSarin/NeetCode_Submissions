# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []
        ptr = head
        while ptr is not None:
            nodes.append(ptr)
            ptr = ptr.next

        if n > len(nodes):
            return head

        if len(nodes) == 1:
            return None

        if len(nodes) == 2 and n==1:
            head.next = None
            return head

        if len(nodes) == 2 and n==1:
            return head.next
        
        if len(nodes)-n == 0:
            return head.next
        
        if n==1: 
            nodes[-2].next = None
            return head

        prev_node = nodes[-n-1]
        next_node = nodes[-n+1]

        prev_node.next = next_node

        return head




        
        