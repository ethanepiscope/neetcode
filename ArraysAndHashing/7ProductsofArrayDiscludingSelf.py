#Comments: dynamic programming :D. O(n), no usage of division operator.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prodInclAndUpTo = [nums[0]]*n #memoizes product of all nums up to and including index i
        prodInclAndAfter = [nums[n-1]]*n #memoizes product of all nums after and including index i

        for i in range(1,n):
            prodInclAndUpTo[i] = nums[i] * prodInclAndUpTo[i-1]
            prodInclAndAfter[n-1-i] = nums[n-1-i] * prodInclAndAfter[n-i]
        
        ret = [prodInclAndAfter[1]] * n
        ret[n-1] = prodInclAndUpTo[n-2]
        for i in range(1,n-1):
            ret[i] = prodInclAndUpTo[i-1] * prodInclAndAfter[i+1]
        return ret

