#this was a great change of pace. O(n)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max = 0
        while l < r:
            if min(heights[l],heights[r]) * (r-l) > max:
                max = min(heights[l],heights[r]) * (r-l)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max