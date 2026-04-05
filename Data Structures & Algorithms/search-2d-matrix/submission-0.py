class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                b.append(matrix[i][j])

        
        l = 0 
        r = len(b) - 1 

        while l <= r:
            mid = (int)((l + r)/2)

            if b[mid] < target:
                l = mid + 1 

            elif b[mid] > target:
                r = mid - 1 

            else:
                return True 

        return False 