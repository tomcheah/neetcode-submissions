# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Add the 2 numbers

        Have a variable that determine whether we need to carry over or not

        Create a node to store the digit 

        Move on and handle the carry over

        Carry over = +1 to next digit
        '''
        dummy = ListNode()
        curr = dummy
        carry_over = 0
        
        while l1 or l2 or carry_over:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0 

            # new digit 
            value = val_1 + val_2 + carry_over
            carry_over = value // 10
            digit = value % 10
            curr.next = ListNode(digit)

            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next