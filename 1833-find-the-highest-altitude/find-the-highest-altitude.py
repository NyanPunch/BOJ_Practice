class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]
        sum = 0
        for i in gain:
            sum += i
            result.append(sum)
        
        return max(result)