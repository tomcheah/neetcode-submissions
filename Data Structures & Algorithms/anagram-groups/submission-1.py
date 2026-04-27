class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Anagram = same letters, diff order 

        Count letter using hashmap 


        """
        frequency_to_sublists = defaultdict(list)

        for string in strs:
            frequency_array = [0 for i in range(26)] # each index maps to a letter
            for letter in string:
                index = ord(letter) - ord('a') # remove offset 
                print(index)
                frequency_array[index] += 1

            frequency_array = tuple(frequency_array) # can't hash mutable lists
            frequency_to_sublists[frequency_array].append(string)

        return list(frequency_to_sublists.values())