class Solution:
    def binarySearch(self, array: List[int], target: int) -> bool:
        l, r = 0, len(array) - 1

        while l <= r:
            m = (l+r) // 2
            if array[m] == target:
                return True
            elif array[m] > target:
                r = m - 1
            else: 
                l = m + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r: 
            m = (l+r) // 2

            curr_arr = matrix[m]
            low, high = curr_arr[0], curr_arr[len(curr_arr)-1]

            if target == low or target == high:
                return True
            elif target > low and target < high:
                return self.binarySearch(curr_arr, target)
            elif target < low:
                r = m - 1
            else:
                l = m + 1

        return False