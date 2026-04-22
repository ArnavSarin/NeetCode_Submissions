# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        curr = head
        ptr = l1
        ptr2 = l2
        
        carry = 0

        while ptr or ptr2 or carry:
            val1 = ptr.val if ptr else 0
            val2 = ptr2.val if ptr2 else 0
            
            total = carry + val1 + val2
            carry = total//10
            total = total % 10

            curr.next = ListNode(total)

            curr = curr.next
            ptr = ptr.next if ptr else None
            ptr2 = ptr2.next if ptr2 else None

        print(carry)

        return head.next



      

