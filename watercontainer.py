class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            maxHeight = min(height[l], height[r])
            maxWidth = r - l

            area = maxHeight * maxWidth
            if area > res:
                res = area

            if height[r] >= height[l]:
                l += 1
            elif height[l] > height[r]:
                r -= 1

        return res