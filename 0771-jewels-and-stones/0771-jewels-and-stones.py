class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        C1= Counter(stones)
        for i in jewels:
            if i in C1:
                c+=C1[i]
        return c
                
        