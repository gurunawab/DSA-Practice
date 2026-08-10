class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, x in enumerate(flowerbed):
            if not x and (i == 0 or not flowerbed[i - 1]) and (i == len(flowerbed) - 1 or not flowerbed[i + 1]):
                flowerbed[i] = 1
                n -= 1
        return n <= 0