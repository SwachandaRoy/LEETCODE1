# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        maxsum=cursum=0
        curr=head
        n=0
        i=0
        lst=[]
        while curr:
            n+=1
            lst.append(curr.val)
            curr=curr.next
        
        while i<n/2:
            twin=lst[n-i-1]
            cursum=lst[i]+twin
            maxsum=max(maxsum, cursum)
            i+=1

        return maxsum

        
