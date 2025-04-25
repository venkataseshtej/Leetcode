class Solution:
    def longestPalindrome(self, s: str) -> int:
        c= Counter(s)
        flag=0
        res=0
        for i in c:
            if c[i] % 2==0:
                res+= c[i]
            else:
                quotient = c[i]//2
                res+= 2*quotient
                # c[i]=='odd'
                flag=1
        if flag==0:
            return res
        else:
            return res+1

        
            


        