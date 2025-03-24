class Solution:
    def partitionString(self, s: str) -> int:
        curr= set()
        res=1
        for c in s:
            if c in curr:
                res +=1
                curr=set()
            curr.add(c)
        return res