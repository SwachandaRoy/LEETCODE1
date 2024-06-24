# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        prev=None
        nxt=None
        count=0
        mid=0
        i=0
        if head.next is None:
            return None

        while curr:
            curr=curr.next
            count+=1
        curr=head
        mid=count//2

        while i<mid-1:
            curr=curr.next
            i+=1
        curr.next=curr.next.next

        return head

        
