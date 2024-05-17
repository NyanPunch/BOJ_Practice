class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums)-1
        result = 0
        nums.sort()
        while start < end:
            sum = nums[start] + nums[end]
            if k == sum:
                result += 1
                start += 1
                end -= 1
            elif k > sum:
                start += 1
            else:
                end -= 1            
        return result