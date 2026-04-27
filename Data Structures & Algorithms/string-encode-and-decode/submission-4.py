class Solution:
    '''
    Define some kind of delimiter

    [{count}{delimiter}{string}]

    Just using count isn't enough b/c what if the number of characters > 9

    Need something to tell us what is end of the count and what is beginning of the string itself
    '''
    delimiter = '@'

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            count = len(string)
            if count == 0:
                # edge case: empty string
                encoded_string += f'{count}{self.delimiter}'
            else:
                encoded_string += f'{count}{self.delimiter}{string}'
        print(f"this is encoded string: {encoded_string}")
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index < len(s):
            char = s[index]
            count_prefix = ''
            while char != self.delimiter: 
                count_prefix += char
                index += 1
                char = s[index]
            count = int(count_prefix)
            index += 1
            curr_string = ""
            if count > 0:
                for i in range(count):
                    curr_string += s[index]
                    index += 1
            res.append(curr_string)

        return res
