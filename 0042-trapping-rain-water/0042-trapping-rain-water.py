class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        m_l = [float('-inf')]*n
        for i in range(1,n):
            m_l[i]= max(m_l[i-1], height[i-1])
        m_r= [float('-inf')]*n
        for j in range(n-2,-1,-1):
            m_r[j]= max(m_r[j+1], height[j+1])
        c=0
        for i in range(1,n):
            k= min(m_r[i],m_l[i]) - height[i]
            if k >0:
                c+=k
        return c







            

        