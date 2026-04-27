class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        NumCharactersString
        """
        encoded_string = ""
        for string in strs:
            length = len(string)
            encoded_string += f"{length}-{string}"
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        pointer = 0
        while pointer < len(s):
            num_chars_to_read = ""
            while s[pointer] != "-":
                num_chars_to_read += s[pointer]
                pointer += 1
            
            pointer += 1 # account for delimiter
            num_chars_to_read = int(num_chars_to_read)

            curr_string = ""
            for i in range(num_chars_to_read):
                curr_string += s[pointer]
                pointer += 1
            decoded_string.append(curr_string)

        return decoded_string
