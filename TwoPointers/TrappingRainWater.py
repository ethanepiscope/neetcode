# Needed to peek at solution to see how two-pointers were used. I stuck with
# my original implementation best I could (with the messy while loops). O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ret = 0
        while l < r:
            #Find left and right local maxes, l and r
            while height[l] <= height[l+1]:
                l += 1
                if l == r: return ret
            while height[r] <= height[r-1]:
                r -= 1
                if r == l: return ret

            #Store indices of local maxes
            left = l
            right = r

            #Fill ret starting from the lower max to guarantee no overfill
            if height[left] < height[right]:
                l += 1
                while height[left] > height[l]:
                    ret += height[left] - height[l]
                    l += 1
                    if l == r: return ret
            else:
                r -= 1
                while height[right] > height[r]:
                    ret += height[right] - height[r]
                    r -= 1
                    if r == l: return ret
        return ret


        