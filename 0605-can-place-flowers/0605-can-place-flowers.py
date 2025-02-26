class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]

        count=0
        # if flowerbed[0]==0 and flowerbed[1]!=1:
        #     count +=1
        #     flowerbed[0]=1
        # elif flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2] !=1:
        #     count +=1
        #     flowerbed[len(flowerbed)-1]=1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i-1] !=1 and flowerbed[i+1]!=1:
                count+=1
                flowerbed[i]=1
        print(count)
        return (count >= n)


        