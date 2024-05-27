class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_cnt = 0

        for num in nums:
            if num != 0:
                total *= num
            else:
                zero_cnt += 1
        
        result = []

        if zero_cnt > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                if zero_cnt == 1:
                    result.append(0)
                else:
                    result.append(total // num)
            else:
                result.append(total)

        return result