class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        c=0
        for j in range(len(s)):
            if i < len(g) and s[j] >= g[i]:
                c+=1
                i+=1         
        # while i < len(g) and j < len(s):
        #     if s[j]>=g[i]:
        #         # c+=1
        #         # j+=1
        #         i+=1
        #     j+=1
        return c



        