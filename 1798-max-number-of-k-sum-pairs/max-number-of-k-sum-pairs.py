class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums)-1
        result = 0
        nums.sort()
        while start < end:
            if k == (nums[start] + nums[end]):
                result += 1
                print(nums[start], nums[end])
                start += 1
                end -= 1
            elif k > nums[start] + nums[end]:
                start += 1
            else:
                end -= 1            
        return result