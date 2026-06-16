import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        Since the array is sorted, the k closest elments will be contiguous in the input array
        '''

        l, r = 0, len(arr) - k

        while l < r:
            mid = (l + r) // 2
            # distance between x and leftmost element of current window [mid:mid+k]
            curr_window_distance = x - arr[mid]

            # distance between x and leftmost element of next possible window [mid+k:]
            next_window_distance = arr[mid+k] - x

            if curr_window_distance > next_window_distance:
                # search within next window
                l = mid + 1
            else:
                # search within current window
                r = mid

        return arr[l:l+k]