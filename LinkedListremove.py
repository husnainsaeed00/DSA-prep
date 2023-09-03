#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, value):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        current=dummy
        while current.next is not None:
            if current.next.val==value:
                current.next=current.next.next
            else:
                current=current.next
        return dummy.next
            
