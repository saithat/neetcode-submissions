# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head):
            return head
        
        prev = head
        next_node = prev.next
        prev.next = None
        while (next_node):
            tmp = next_node.next
            next_node.next = prev
            prev = next_node
            next_node = tmp
        return prev
