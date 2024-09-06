# Was gonna try to do dynamic programming, but i think you can't beat
#O(n^2) runtime so why waste the space lol
#Update turns out I forgot that hashmaps exist


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return 0