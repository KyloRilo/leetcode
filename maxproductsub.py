class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMin, curMax = 1, 1

        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue

            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            result = max(result, curMax, curMin)

        return result