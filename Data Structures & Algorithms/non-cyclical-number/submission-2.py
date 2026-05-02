class Solution:
    def isHappy(self, n: int) -> bool:
        string_num = str(n)
        digits = [int(digit) for digit in string_num]
        seen_sums = set()

        res = 0 
        count = 0
        while res != 1:
            squares = [digit**2 for digit in digits]
            res = sum(squares)
            seen_sums.add(res)
            string_num = str(res)
            print(string_num)
            digits = [int(digit) for digit in string_num]
            print(f'{count=}')
            count += 1
            print(seen_sums)
            if count >= 35:
                return False

        print(f'{res=}')
        return res == 1

        
