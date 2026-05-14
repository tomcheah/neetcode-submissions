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

        How to handle cases where l1 and l2 are not the same length? 
        - Just copy over the rest of the digits while handling the carry over?

        Carry over = +1 to next digit

        
        '''
        dummy = ListNode()
        carry_over = False
        prev = dummy

        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                value = l1.val
                l1 = l1.next
            elif l2:
                value = l2.val
                l2 = l2.next
        
            ## this is not right 
            if carry_over: 
                value += 1
                carry_over = False
            
            digit = value
            if value > 9:
                digit = value % 10
                carry_over = True

            node = ListNode(digit)
            prev.next = node
            prev = prev.next
            
        # handle last one item
        if carry_over:
            node = ListNode(1)
            prev.next = node
            prev = prev.next

        return dummy.next