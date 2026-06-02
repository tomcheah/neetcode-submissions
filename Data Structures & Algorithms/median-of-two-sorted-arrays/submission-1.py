class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        # binary search on the smaller array A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # pointer for A -> number of elements in left partition for A
            j = half - i - 2 # number of elements in B (need -2 to account for i and indexing starting from 0)

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i+1] if (i+1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if (j+1) < len(B) else float('infinity')

            # we've found valid partitions
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # too many elements in smaller array
            elif Aleft > Bright:
                r = i - 1
            # not enough elements in smaller array
            else:
                l = i + 1 

                


        

