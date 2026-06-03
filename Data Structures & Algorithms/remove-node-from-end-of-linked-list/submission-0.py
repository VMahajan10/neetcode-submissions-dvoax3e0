# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        cur = head 
        while cur:
            len = len + 1
            cur = cur.next 
        #Traverse to find total length of the list 



        spot = len - n
        
        x = head 
        if spot == 0:
            return  head.next
        for i in range(len - 1):
            if i + 1 == spot:
                x.next = x.next.next
            else:
                x = x.next 
        
        return head



