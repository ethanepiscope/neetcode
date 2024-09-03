class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 0
            s_dict[char] += 1
        for char in t:
            if char not in s_dict:
                return False
            s_dict[char] -= 1
        for key in s_dict:
            if s_dict[key] != 0:
                return False
        return True