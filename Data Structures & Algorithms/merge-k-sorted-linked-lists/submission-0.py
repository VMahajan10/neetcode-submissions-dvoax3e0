# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
            #Check if a list even exists 
        return self.divide(lists, 0, len(lists) - 1)
        #call first divide 

    def divide(self, l, left, right):
        if right < left:
            return None
            #make sure left < right 
        
        if right == left:
            #return the value if right == left 
            #because they will be equal 
            return l[left]

        m = left + (right - left)//2
        #calculate the mid point 

        x = self.divide(l, left, m)
        #call recursive divide commands to split the list even further
        y = self.divide(l, m + 1, right)

        return self.conquer(x, y)

    def conquer(self, a, b):
        dummy = ListNode(0)
        cur = dummy 
        #instantiate the pointer node 

        while a and b:
            #Merge based on which value is smaller 
            if a.val < b.val:
                cur.next = ListNode(a.val)
                a = a.next

            else:
                cur.next = ListNode(b.val)
                b = b.next
            
            cur = cur.next
        
        #if one list is still longer
        #then you put it at the end 
        if a:
            cur.next = a 

        if b:
            cur.next = b 

        return dummy.next
        #Return the first value of the list 

            


