from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Use Counters somehow 

        Turn all the strings into counters

        And then group them together somehow

        How can we group them together? 

        Can we do a hashmap where it's like: 

        [Counter] -> List[string] 

        And then turn it back into a list

        Problem: Can't use a counter for a hashmap key
        Solution: Use a frequency array as the key

        '''
        def get_frequency_array(string: str) -> List[str]: 
            frequency_array = [0 for i in range(26)]
            for char in string:
                char_index = ord(char) - ord('a')
                frequency_array[char_index] += 1
            return frequency_array


        grouped_anagrams = defaultdict(list)

        for string in strs:
            frequency_array = tuple(get_frequency_array(string))
            grouped_anagrams[frequency_array].append(string)
      
        return list(grouped_anagrams.values())
