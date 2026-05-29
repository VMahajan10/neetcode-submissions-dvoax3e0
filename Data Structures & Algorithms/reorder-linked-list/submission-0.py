# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next 

        #Utilize linked list cycle 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        #Reverse the second half of the list 
        a = slow.next
        prev = slow.next = None

        while a:
            temp = a.next 
            a.next = prev 
            prev = a 
            a = temp 
        
        #Merge the two lists together 
        first = head 
        second = prev  
        
        while second:

            temp1 = first.next
            temp2 = second.next

            first.next = second
            #point to the first second node 
            second.next = temp1 
            #then point to the next first node val

            first = temp1
            second = temp2




        
        