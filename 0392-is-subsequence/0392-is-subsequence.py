class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=len(s)
        b=len(t)
        if a > b:
            return False
        if a ==0:
            return True
        i=0
        for j in range(b):
            if s[i] == t[j] :
                if i == a-1:
                    return True
                i+=1
    
        return False
        