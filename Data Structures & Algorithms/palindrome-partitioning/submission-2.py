class Solution:

    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(start: int, path: List[str]) -> None:
            if start == len(s):
                res.append(path[:])

            for end in range(start, len(s)):
                substring = s[start:end+1]
                if self.is_palindrome(substring):
                    path.append(substring)
                    helper(end+1, path)
                    path.pop()

        helper(0, []) 
        return res