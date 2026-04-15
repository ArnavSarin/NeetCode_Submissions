# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr_a = list1
        ptr_b = list2

        ans, head = None, None

        if ptr_a == None:
            return ptr_b
        elif ptr_b == None:
            return ptr_a
        elif ptr_a.val >= ptr_b.val:
            ans = ptr_b
            head = ptr_b
            ptr_b = ptr_b.next
        else:
            ans = ptr_a
            head = ptr_a
            ptr_a = ptr_a.next
        
        while ptr_a != None and ptr_b != None:
            if ptr_a.val >= ptr_b.val:
                head.next = ptr_b
                ptr_b = ptr_b.next
            else:
                head.next = ptr_a
                ptr_a = ptr_a.next

            head = head.next

        while ptr_a != None:
            head.next = ptr_a
            ptr_a = ptr_a.next
            head = head.next

        while ptr_b != None:
            head.next = ptr_b
            ptr_b = ptr_b.next
            head = head.next

        return ans

        
