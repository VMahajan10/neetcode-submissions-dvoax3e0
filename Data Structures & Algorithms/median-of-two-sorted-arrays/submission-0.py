class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 
        B = nums2 


        total = len(nums1) + len(nums2)

        if len(nums2) < len(nums1):
            A = nums2
            B = nums1

        l = 0 
        r = len(A) - 1 
        half = total//2

        while True:
            mid = (l + r)//2
            part = half - mid - 2 
            #(i + 1) + (j + 1) = half
            #did i + 1 and j + 1 to remove 0 based indexing  
            #j = half - i - 2 

            if mid >= 0:
                Aleft = A[mid]
                #We found the biggest value on the left side

            else:
                Aleft = float("-infinity")

            if mid + 1 < len(A):
                Aright = A[mid + 1]
                #Smallest value on the right side 

            else:
                Aright = float("infinity")

            if part >= 0:
                Bleft = B[part]

            else:
                Bleft = float("-infinity")

            if part + 1 < len(B):
                Bright = B[part + 1]

            else:
                Bright = float("infinity")

            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)

                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2

            elif Aleft > Bright:
                r = mid - 1 

            else:
                l = mid + 1 
            