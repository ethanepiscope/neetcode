#Diorgano


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        g = set()
        for num in nums:
            g.add(num)
        return len(g) != len(nums)