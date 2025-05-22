class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        se=set()
        maxx=0
        for right in range(len(s)):
            while s[right] in se:
                se.remove(s[left])
                left+=1
            se.add(s[right])
            l=right-left+1
            maxx=max(maxx,l)
        return maxx

            
                