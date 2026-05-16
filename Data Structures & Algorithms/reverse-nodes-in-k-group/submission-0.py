# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Reversing nodes in a linked list is simple 

        Brute force:
        - Check for next k nodes
        - If next k nodes exist, reverse the k nodes 
        - Repeat until done

        What do we need to do to reverse the k nodes?

        Classic reverse:
            temp = curr.next
            curr.next = prev
            prev = curr  
            curr = temp

        Important part:
        - After reversing, connect the tail of the reversed part to the next node the list

        For each k groups, we need: 
        - group_prev (the original group's prev)
        - group_next (the original group's next)
        - group_head (the original group's start)
        - group_end (aka the kth node)
        
        group_head becomes the tail 
        group_head.next = group_next

        previous node connects to the new head of this group
        group_prev.next = group_end 

        everything else in the middle gets reversed as normal

        '''
        dummy = ListNode(next=head)
        group_prev = dummy
        while self.has_next_k(head, k):
            group_head = head

            # move head forward k-1 times to get the original next
            for _ in range(k-1):
                head = head.next

            group_tail = head
            group_next = head.next
            self.reverse_nodes(group_head, group_tail, group_prev, group_next, k)
            
            # move on
            head = group_next

            # the next prev is the original head of the previous group (aka the reversed tail)
            group_prev = group_head
            

        return dummy.next

    def has_next_k(self, head: Optional[ListNode], k: int) -> bool:
        for i in range(k):
            if not head:
                return False
            
            head = head.next

        return True

    def reverse_nodes(self, group_head, group_tail, group_prev, group_next, k) -> None:
        prev = None
        curr = group_head

        # reverse the nodes
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        group_prev.next = group_tail
        group_head.next = group_next        
            
