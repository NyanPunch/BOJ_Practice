class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        f, s = inf, inf

        for t in nums:
            if s < t: return True
            if t <= f: f = t
            else: s = t

        return False