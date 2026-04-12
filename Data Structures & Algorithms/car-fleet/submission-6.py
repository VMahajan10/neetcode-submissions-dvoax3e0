class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = list(zip(position,speed))
        pairs.sort(reverse=True)

        for i, j in pairs:
            m = ((target - i)/j)

            stack.append(m)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

            
        



        





        



        


        
        

       



        
            


       
        

       

        
        