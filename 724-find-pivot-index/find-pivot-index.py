class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_total = 0
        
        l = 0
        while l < len(nums):
            right_total = total - left_total - nums[l]

            if left_total == right_total:
                return l
            
            left_total += nums[l]
            l += 1

        return -1