class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        for i in range(k):
            currSum += nums[i]
        maxSum = currSum
        l = 0
        r = k
        while r < len(nums):
            currSum -= nums[l]
            l += 1
            currSum += nums[r]
            r += 1
            maxSum = max(currSum, maxSum)
        return maxSum/k