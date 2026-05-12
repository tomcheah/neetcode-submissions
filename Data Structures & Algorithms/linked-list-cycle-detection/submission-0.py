# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            if not fast.next:
                return False 
            fast = fast.next.next

            if slow == fast:
                return True
        return False