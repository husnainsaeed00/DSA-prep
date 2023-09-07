# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        # Move to the node just before the sub-list to be reversed.
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse the sub-list from left to right.
        current = prev.next
        for _ in range(right - left):
            temp = prev.next
            prev.next = current.next
            current.next = current.next.next
            prev.next.next = temp
        
        return dummy.next
            
