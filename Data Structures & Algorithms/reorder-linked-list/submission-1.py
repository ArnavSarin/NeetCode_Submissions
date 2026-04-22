# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []

        ptr = head
        while ptr is not None:
            nodes.append(ptr)
            ptr = ptr.next
        
        ptr = head
        for i in range(0,len(nodes)+1//2):
            if i%2 == 0:
                head.next = nodes[-(i//2+1)]
            else:
                head.next = nodes[(i//2)+1]
            head = head.next
        
        head.next = None
        
        head = ptr
        







            

        


        