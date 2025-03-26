class Solution:
    def countBits(self, n: int) -> List[int]:
        def x(i):
            k=str(bin(i))
            k=k[2:]
            return sum([int(i) for i in k])
        l=[]
        for a in range(n+1):
            l.append(x(a))
        return l
        def x(i):
            k=str(bin(i))
            return sum([int(i) for i in k])



        