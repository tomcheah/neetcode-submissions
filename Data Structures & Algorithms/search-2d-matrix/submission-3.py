class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Binary search through the rows 

        Then binary search within a row
        '''

        l, r = 0, len(matrix) - 1
        # find our row
        while l <= r:
            mid = (l+r) // 2
            mid_row = matrix[mid]
            mid_low, mid_high = mid_row[0], mid_row[-1]

            # we've found our target
            if mid_low <= target <= mid_high:
                break

            elif target < mid_low:
                r = mid-1

            elif target > mid_high:
                l = mid + 1
            
        # binary search within the row
        mid_l, mid_r = 0, len(mid_row)-1
        while mid_l <= mid_r:
            mid = (mid_l + mid_r) // 2

            if target == mid_row[mid]:
                return True

            elif target < mid_row[mid]:
                mid_r = mid - 1

            elif target > mid_row[mid]:
                mid_l = mid + 1
        
        return False