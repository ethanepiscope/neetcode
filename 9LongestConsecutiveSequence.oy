#I couldn't think of an O(n) solution on my own so I looked at the provided solution :(
#Initially thought there was an issue if we had many elements that were the start of a sequence,
#but since sets don't permit duplicates this wasnt and issue

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        longestSeq = 0
        for n in uniqueNums:
            if (n - 1) not in uniqueNums:
                currentLength = 1
                while (n + currentLength) in uniqueNums:
                    currentLength += 1
                longestSeq = max(currentLength, longestSeq)
        return longestSeq