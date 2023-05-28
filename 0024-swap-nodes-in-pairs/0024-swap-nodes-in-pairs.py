# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head==None or head.next==None:
            return head
        # dealing with the other case - for even and odd no of nodes
        curr=head
        while(curr.next!=None ):
            #swapping 
            curr.val,curr.next.val=curr.next.val,curr.val
            # moving two nodes ahead after swap
            if curr.next.next:
                curr=curr.next.next
            else:
                break
        return head
        