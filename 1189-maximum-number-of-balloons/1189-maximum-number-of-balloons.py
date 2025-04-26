class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        if len(text) < 6:
            return 0
        s='balloon'
        c2=Counter(s)
        c1= Counter(text)     
        m = []
        for i in c2:
            if i not in c1:
                return 0
            else:
                m.append(c1[i]//c2[i])
        return min(m)


        