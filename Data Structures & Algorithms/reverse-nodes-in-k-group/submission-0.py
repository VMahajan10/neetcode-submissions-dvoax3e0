# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy 

        while True:
            kthNode = self.getKthNode(groupPrev, k)
            if not kthNode:
                break 

            groupNext = kthNode.next 

            cur = groupPrev.next 
            prev = kthNode.next 
            
            while cur != groupNext:
                temp = cur.next
                cur.next = prev 
                prev = cur 
                cur = temp 

            temp = groupPrev.next 

            groupPrev.next = kthNode 

            groupPrev = temp 

        
        return dummy.next



    def getKthNode(self, cur, k):
        while cur and k > 0:
            cur = cur.next 
            k = k - 1 
        return cur 


    