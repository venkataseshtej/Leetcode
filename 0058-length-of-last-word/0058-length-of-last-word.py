class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        i= len(s)-1
        while i >= 0:
            if (s[i] ==' ') and (c==0):
                i-=1
            elif s[i] != " ":
                c +=1
                i-=1
            else:
                return c
        return c

        