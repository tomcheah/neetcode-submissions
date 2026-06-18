class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def helper(i: int, j: int) -> int:
            # pointer for s3 is implicit
            k = i + j

            if k == len(s3):
                # we must use up all characters in s1 and s2
                return i == len(s1) and j == len(s2)
        
            if (i, j) in dp:
                return dp[(i, j)]

            use_s1 = False
            if i < len(s1) and s1[i] == s3[k]:
                use_s1 = helper(i+1, j)

            use_s2 = False
            if j < len(s2) and s2[j] == s3[k]:
                use_s2 = helper(i, j+1)

            dp[(i, j)] = use_s1 or use_s2
            return dp[(i, j)]

        return helper(0, 0)