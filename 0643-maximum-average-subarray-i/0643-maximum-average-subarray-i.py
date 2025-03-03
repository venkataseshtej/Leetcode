class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l= len(nums)
        m= sum(nums[:k])
        final= m/k
        for i in range(1,l-k+1):
            m = m-nums[i-1]
            m = m+ nums[i+k-1]
            final = max(final, m/k)
        return final
        