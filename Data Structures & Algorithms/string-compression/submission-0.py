class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed_string = ''
        curr_char = None
        count = 0
        write = 0

        for i, char in enumerate(chars):
            if not curr_char: 
                curr_char = char
                count = 1
            elif curr_char == char:
                count += 1
            elif char != curr_char:
                if count == 1:
                    chars[write] = curr_char
                    write += 1
                else:
                    chars[write] = curr_char
                    write += 1
                    for c in str(count):
                        chars[write] = c
                        write += 1
                
                curr_char = char
                count = 1
            
        if curr_char and count:
            if count == 1:
                chars[write] = curr_char
                write += 1
            else:
                chars[write] = curr_char
                write += 1
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write