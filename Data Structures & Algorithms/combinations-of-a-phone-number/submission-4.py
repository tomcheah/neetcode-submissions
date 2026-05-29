class Solution:
    digit_to_letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res

        def dfs(i: int, path: str) -> None: 
            if i >= len(digits):
                res.append(path)
                return

            for letter in self.digit_to_letters[digits[i]]:
                dfs(i+1, path + letter)
                
        dfs(0, '')
        return res