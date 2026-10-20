class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxim = 0
        for candy in candies:
            if candy > maxim: maxim = candy
        
        return [True if candy+extraCandies >= maxim else False for candy in candies]