class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import Counter
        dct = Counter(s)
        ans=[]
        st = set()
        l,r = 0,0
        while r < len(s):
            st.add(s[r])
            dct[s[r]] -= 1
            if dct[s[r]]== 0:
                st.remove(s[r])
            if len(st) == 0:
                ans.append(r-l+1)
                l = r+1
            r +=1
        return ans 
        