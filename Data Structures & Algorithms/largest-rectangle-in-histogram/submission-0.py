class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        res = 0 

        for i in range(n + 1):
            #looping until the stack ends fully so that way we can account 
            #for even the very last variable 
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                #pop until we find the nearest smaller value 
                height = heights[stack.pop()]

                if not stack:
                    #if we have the smallest value for now
                    width = i
                    #set the width to i 
                else:
                    #if there is a value still in the stack 
                    width = i - stack[-1] - 1

                res = max(res, height*width)

            stack.append(i)

                

        return res
        

        
     

