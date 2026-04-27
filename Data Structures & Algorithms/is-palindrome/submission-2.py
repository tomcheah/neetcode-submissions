class Solution:
    def isPalindrome(self, s: str) -> bool:
        # prep the string -> alphanumeric only, no spaces, lowercase
        stripped_string = "".join(char for char in s if char.isalnum()).lower()
        l, r = 0, len(stripped_string) - 1
        while l < r:
            if stripped_string[l] != stripped_string[r]:
                return False
            l += 1
            r -= 1

        return  True