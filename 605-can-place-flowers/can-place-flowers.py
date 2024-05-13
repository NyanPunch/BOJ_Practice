class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        length = len(flowerbed)
        if length-1 == i and flowerbed[i] == 0:
            return True
        while i < length:
            if flowerbed[i] == 0:
                nxt = flowerbed[i+1] if i < length - 1 else 0
                if nxt == 0:
                    i += 2
                    n -= 1
                else:
                    i += 1
                if n <= 0: return True
            else:
                i += 2
            
        return n <= 0