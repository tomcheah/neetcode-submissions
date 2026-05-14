# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        We need a dummy node in case we need to delete the initial start

        Starting slow at dummy gets us to (n-1)th node, saving us from off by 1 error
        '''
        dummy = ListNode(next=head)
        slow, fast = dummy, head
        for _ in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next

        # remove the node
        slow.next = slow.next.next

        return dummy.next












