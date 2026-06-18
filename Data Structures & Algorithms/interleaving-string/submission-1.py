class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def helper(i: int, j: int, k: int):
            # ran out of characters from s1
            if i == len(s1):
                return s2[j:] == s3[k:]

            if j == len(s2):
                return s1[i:] == s3[k:]

            if k == len(s3) and i < len(s1) and j < len(s2):
                return False

            if (i, j, k) in dp:
                return dp[(i, j, k)]

            if s1[i] != s3[k] and s2[j] != s3[k]:
                return False

            use_s1 = False
            if s1[i] == s3[k]:
                use_s1 = helper(i+1, j, k+1)

            use_s2 = False
            if s2[j] == s3[k]:
                use_s2 = helper(i, j+1, k+1)

            dp[(i, j, k)] = use_s1 or use_s2
            return dp[(i, j, k)]

        return helper(0, 0, 0)