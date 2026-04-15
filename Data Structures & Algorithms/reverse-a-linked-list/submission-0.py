# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
    
        arr = []

        while head != None:
            arr.append(head)
            head = head.next
            
        ans, head = arr[-1], arr[-1]

        for i in range(len(arr)-2,-1,-1):
            head.next = arr[i]
            head = head.next

        head.next = None
        return ans


