#My thoughts: python is a strange and terrifying language

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_to_word = {}
        for s in strs:
            letterCount = {}
            for letter in s:
                letterCount[letter] = 1 + letterCount.get(letter, 0)
            key = tuple(sorted(letterCount.items()))
            if key in count_to_word:
                count_to_word[key].append(s)
            else:
                count_to_word[key] = [s]
        return count_to_word.values()