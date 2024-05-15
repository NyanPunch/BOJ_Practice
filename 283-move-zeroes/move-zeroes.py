class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = len(nums)
        
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] == 0:
                    nums[i], nums[j] = nums[j], nums[i]

        