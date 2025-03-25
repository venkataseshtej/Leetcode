class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        old=0
        prev=1
        just=1
        for i in range(3,n+1):
            curr= old+prev+just
            old= prev
            prev,just =just, curr
        return curr




        
        