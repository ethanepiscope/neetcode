#O(nlogn) solution that repurposes previous elements in the array to perform binary search on. I simply
#did not see the O(n) solution sadly. I am glad I got to do a binary search tho.

from math import floor

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = -1 #right bound on BinSearch
        for j in range(len(numbers)):
            if (k := self.BinSearch(numbers, i, numbers[j])) != -1:
                return [k+1, j+1]
            numbers[j] = target - numbers[j]
            i = j
        return [-1,-1]

    def BinSearch(self, numbers: List[int], right_idx: int, target: int) -> int:
        left_idx = 0
        while left_idx <= right_idx:
            mid = floor((left_idx + right_idx)/2)
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                right_idx = mid - 1
            else:
                left_idx = mid + 1
        return -1 



