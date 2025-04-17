class Solution:
    def climbStairs(self, n: int) -> int:
        d={1:1, 2:2}

        def climb(n):
            if n in d:
                return d[n]
            else:
                d[n]= climb(n-1)+climb(n-2)
                return d[n]
        return climb(n)
    

        