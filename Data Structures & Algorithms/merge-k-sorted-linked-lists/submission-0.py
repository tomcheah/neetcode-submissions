# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Divide and conquer 

        Each merge = O(N) work

        Takes O(logk) merges 

        Runtime = O(Nlogk)
        '''

        def mergeKListsHelper(lists: List[Optional[Listnode]], left: int, right: int) -> Optional[ListNode]:
            if not lists:
                return None
            
            if left == right:
                return lists[left]

            mid = (left+right) // 2
            merged_left = mergeKListsHelper(lists, left, mid)
            merged_right = mergeKListsHelper(lists, mid+1, right)

            return self.mergeLists(merged_left, merged_right)

        return mergeKListsHelper(lists, 0, len(lists)-1)


    def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        if l1:
            head.next = l1
        elif l2:
            head.next = l2

        return dummy.next








