class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums: List[int]) -> List[int]:
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return merge(left, right)

        def merge(left: List[int], right: List[int]) -> List[int]:
            res = []
            l, r = 0, 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

            res.extend(left[l:])
            res.extend(right[r:])

            return res


        return merge_sort(nums)