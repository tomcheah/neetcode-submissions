class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer solution
        front, end = 0, len(s)-1
        while front < end:
            # handle non-alphanumeric

            # TODO: handle out of bounds?
            if not s[front].isalnum():
                front += 1
                continue

            if not s[end].isalnum():
                end -= 1
                continue

            if s[front].lower() == s[end].lower():
                print(f"{s[front] =}, {s[end] =}")
                front += 1
                end -=1
            else:
                print("we are here")
                print(f"{s[front] =}, {s[end] =}")

                return False

        return True