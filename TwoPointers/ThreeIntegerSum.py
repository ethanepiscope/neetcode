#roughly n^2 solution. n^3 technically because checking if the list is in ret
#is n time. I would normally make ret a set and just pass it arrays to hash, but i
#didn't want to import the arrays package lol. worst case is only an issue 
#if there are a lot of combos to make zero

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:    
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    if sorted([nums[i],nums[j],nums[k]]) not in ret:
                        ret.append(sorted([nums[i],nums[j],nums[k]]))
                    j += 1
                    k -= 1
        return list(ret)
        