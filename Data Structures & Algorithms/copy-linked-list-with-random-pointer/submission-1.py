"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Use a hashmap to map the original node to its copy
        - We'll use this to update the random pointer of the copied list in the 2nd pass
        '''
        dummy = Node(0)
        previous_copy = dummy

        original = head
        original_to_copy = {} # map original node -> copied node
        original_to_copy[None] = None

        # create copy filled out with copy.next
        while original:
            copy = Node(x=original.val)
            original_to_copy[original] = copy
            previous_copy.next = copy
            previous_copy = copy
            original = original.next

        # fill in copy.random
        original = head
        while original:
            copy = original_to_copy[original]
            # handle null case
            if original.random:
                copy.random = original_to_copy[original.random]
            else:
                copy.random = None
            original = original.next

        return original_to_copy[head]
        