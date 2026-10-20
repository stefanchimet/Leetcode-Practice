class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        left  = n
        for i in range(len(flowerbed)):  
            if flowerbed[i] == 0:
                left_free = i==0 or flowerbed[i-1]==0
                right_free = i==len(flowerbed)-1 or flowerbed[i+1]==0

                if left_free and right_free:
                    left-=1
                    flowerbed[i]=1
        
        return left<=0


        