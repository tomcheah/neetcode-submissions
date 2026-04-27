from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_frequency_array(string: str) -> List[str]: 
            frequency_array = [0 for i in range(26)]
            for char in string:
                char_index = ord(char) - ord('a')
                frequency_array[char_index] += 1
            return frequency_array

        grouped_anagrams = defaultdict(list)

        for string in strs:
            # can't use mutable lists or objects as dictionary keys -> convert to tuple
            frequency_array = tuple(get_frequency_array(string))
            grouped_anagrams[frequency_array].append(string)
      
        return list(grouped_anagrams.values())
