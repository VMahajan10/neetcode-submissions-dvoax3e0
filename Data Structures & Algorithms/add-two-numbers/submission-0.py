# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        #Set up the dummy pointer 
        carry = 0 

        while l1 or l2 or carry:
            #We want to run if there are still values in l1 or l2
            #or if there is a carrry so that way we can place it 
            #into its own node 
            #Check to see if the value for list1 exists 
            if l1:
                val1 = l1.val
            else:
                val1 = 0 
            
            #Check to see if the value for list2 exists 
            if l2:
                val2 = l2.val
            else:
                val2 = 0 
   
            #Find the sum 
            sum = val1 + val2 + carry 
            #If sum > 10 we need to carry over 1 
            carry = sum // 10
            #Take the last digit 
            sum = sum % 10

            #store the one digit sum value in the list 
            cur.next = ListNode(sum)
            #Move the list 
            cur = cur.next 

            if l1:
                l1 = l1.next 
                #move to the next value of l1 if it exists 
            else:
                l1 = None 
            
            if l2:
                l2 = l2.next 
                #move to the next value of l1 if it exists 
            else:
                l2 = None
        
        return dummy.next
        #Return first value of result list 
