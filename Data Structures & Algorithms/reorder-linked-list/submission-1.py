# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Use fast and slow pointers to find the middle of the linked list

        Reverse the second half of the linked list

        Merge the 2 linked lists in alternate fashion
        '''

        # find middle of linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linked list
        l, r = None, slow.next
        while r:
            temp = r.next
            r.next = l
            l = r
            r = temp

        slow.next = None
        # merge the 2 linked lists in alternate fashion
        forward, rev = head, l
        while rev:
            forward_next_original = forward.next
            rev_next_original = rev.next
            forward.next = rev
            rev.next = forward_next_original
            rev = rev_next_original
            forward = forward_next_original